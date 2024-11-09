import copy
import tkinter as tk
from game import gameState
from Agents import AlphaBetaAgent
import time

CELL_SIZE = 60  # 每个棋盘格的大小
BOARD_SIZE = 8 * CELL_SIZE  # 棋盘的总大小


class OthelloGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Othello Game")
        self.canvas = tk.Canvas(self.root, width=BOARD_SIZE, height=BOARD_SIZE)
        self.canvas.pack()

        self.game = gameState()
        self.agentEnabled = True
        self.alpha_beta_agent = AlphaBetaAgent() if self.agentEnabled else None

        # 绘制初始棋盘
        self.draw_board()
        self.update_player_label()

        # 开始游戏循环
        self.game_loop()

    def draw_board(self, last_x=None, last_y=None):
        """绘制棋盘和棋子，并标记合法移动"""
        self.canvas.delete("all")  # 清除当前画布

        # 画出棋盘的格子
        for i in range(8):
            for j in range(8):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")

                # 画出棋子
                if self.game.board[i][j] == 1:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="black")
                elif self.game.board[i][j] == -1:
                    self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="white")

        # 获取当前玩家和合法的移动
        suc = copy.deepcopy(self.game)
        suc.timeInc()
        player = suc.getPlayer()
        legal_moves = suc.getPlayPosition(player)

        # 标记合法位置
        for (x, y) in legal_moves:
            x1, y1 = y * CELL_SIZE, x * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=2)

        # 标记上一次的移动
        if last_x is not None and last_y is not None:
            x1, y1 = last_y * CELL_SIZE, last_x * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=2)

    def game_loop(self):
        """基于 main.py 的逻辑进行循环判断"""
        while True:
            self.game.timeInc()
            player = self.game.getPlayer()
            legal_moves = self.game.getPlayPosition(player)

            # 如果没有合法动作，自动跳过回合
            if legal_moves == []:
                if self.game.numWhite + self.game.numBlack == 64:
                    self.end_game()
                    break
                self.draw_board()
                self.root.update()  # 更新界面显示 AI 的操作
                continue

            # 判断是否轮到 AI
            if self.agentEnabled and player == -1:
                x, y = self.alpha_beta_agent.getAction(self.game)
                self.game.update(x, y, player)
                self.draw_board(x, y)
                self.root.update()  # 更新界面显示 AI 的操作
                time.sleep(0.1)  # 延迟 0.5 秒以便视觉反馈
            else:
                # 等待玩家点击合法位置
                x, y = self.get_player_action(legal_moves)
                self.game.update(x, y, player)
                self.draw_board(x, y)
                self.root.update()  # 更新界面显示玩家的操作

            # 检查游戏是否结束
            if self.check_game_over():
                break

    def get_player_action(self, legal_moves):
        """等待玩家点击一个合法位置"""
        self.player_click_position = None
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # 等待玩家选择一个合法位置
        while self.player_click_position not in legal_moves:
            self.root.update()
            time.sleep(0.1)

        # 解绑点击事件
        self.canvas.unbind("<Button-1>")
        return self.player_click_position

    def on_canvas_click(self, event):
        """处理玩家点击事件"""
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        self.player_click_position = (row, col)  # 记录点击位置

    def update_player_label(self):
        """更新玩家标签（在 GUI 中可扩展）"""
        player = self.game.getPlayer()
        print("Current Player:", "Black" if player == 1 else "White")

    def check_game_over(self):
        """检查游戏是否结束"""
        if self.game.numWhite + self.game.numBlack == 64 or not (
                self.game.getPlayPosition(1) or self.game.getPlayPosition(-1)):
            self.end_game()
            return True
        return False

    def end_game(self):
        """显示游戏结束信息"""
        winner = "Black" if self.game.numBlack > self.game.numWhite else "White"
        print(f"Game Over! {winner} wins!")
        self.canvas.unbind("<Button-1>")  # 禁用点击事件


def main():
    root = tk.Tk()
    gui = OthelloGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
