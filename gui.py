import copy
import tkinter as tk
from game import gameState
import time
from Agents import AlphaBetaAgent

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

        # 为每个格子绑定点击事件
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.draw_board(4, 4)

    def draw_board(self, x0, y0):
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
        suc.time += 1
        player = suc.getPlayer()
        legal_moves = suc.getPlayPosition(player)

        # 标记合法位置
        for (x, y) in legal_moves:
            x1, y1 = y * CELL_SIZE, x * CELL_SIZE  # 注意这里的 (y, x) 转换
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=2)
        x1, y1 = y0 * CELL_SIZE, x0 * CELL_SIZE  # 注意这里的 (y, x) 转换
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=2)

    def on_canvas_click(self, event):
        self.game.time += 1
        # 计算点击的棋盘坐标
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        player = self.game.getPlayer()

        legal_moves = self.game.getPlayPosition(player)
        if legal_moves == []:
            print("You can't move")
            self.game.time += 1
            x, y = self.alpha_beta_agent.getAction(self.game)
            self.game.update(x, y, -1)
            self.draw_board(x, y)
            return

        if (row, col) not in legal_moves:
            print("Invalid move!")
            return

        # 更新棋盘状态并绘制
        self.game.update(row, col, player)
        self.draw_board(row, col)
        self.root.update()

        # 检查游戏是否结束
        if self.game.numWhite + self.game.numBlack == 64 or not legal_moves:
            print("Game Over")
            self.canvas.unbind("<Button-1>")
            return

        # AI 回合
        if self.agentEnabled and self.game.getPlayer() == 1:
            self.game.time += 1
            if self.game.getPlayPosition(1) == []:
                return
            x, y = self.alpha_beta_agent.getAction(self.game)
            self.game.update(x, y, -1)
            self.draw_board(x, y)
            self.root.update()


def main():
    root = tk.Tk()
    gui = OthelloGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
