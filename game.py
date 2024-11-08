
class gameState:
    def __init__(self):
        self.numWhite = 2
        self.numBlack = 2
        self.board = [[0 for i in range(8)] for j in range(8)]
        self.board[3][3] = -1#white agent
        self.board[3][4] = 1#Black player
        self.board[4][3] = 1
        self.board[4][4] = -1
        self.whitePos = [(3, 3), (4, 4)]
        self.blackPos = [(3, 4), (4, 3)]
        self.time = -1

    def timeInc(self):
        self.time += 1
    def getBoard(self):
        return self.board

    def getPlayer(self):
        return 1 if self.time%2 == 0 else -1

    def getPlayPosition(self, player):
        board = self.board
        result = []
        #player = self.getPlayer()
        if player == -1:
            for x, y in self.whitePos:
                x0 = x
                y0 = y
                while x0-1>0 and self.board[x0-1][y0] == 1:
                    x0 -= 1
                x0 -= 1
                if x0 >= 0 and board[x0][y0] == 0 and x0!=x-1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while y0-1>=0 and self.board[x0][y0-1] == 1:
                    y0 -= 1
                y0 -= 1
                if y0 >= 0 and board[x0][y0] == 0 and y0!=y-1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while x0+1<=7 and self.board[x0+1][y0] == 1:
                    x0 += 1
                x0 += 1
                if x0 <= 7 and board[x0][y0] == 0 and x0!=x+1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while y0+1<=7 and self.board[x0][y0+1] == 1:
                    y0 += 1
                y0 += 1
                if y0 <= 7 and board[x0][y0] == 0 and y0!=y+1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while x0-1>=0 and y0-1>=0 and self.board[x0-1][y0-1] == 1:
                    y0 -= 1
                    x0 -= 1
                y0 -= 1
                x0 -= 1
                if x0>=0 and y0>=0 and board[x0][y0] == 0 and y0!=y-1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while x0-1>=0 and y0+1<=7 and self.board[x0-1][y0+1] == 1:
                    y0 += 1
                    x0 -= 1
                y0 += 1
                x0 -= 1
                if x0>=0 and y0<=7 and board[x0][y0] == 0 and y0!=y+1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while x0+1<=7 and y0-1>=0 and self.board[x0+1][y0-1] == 1:
                    y0 -= 1
                    x0 += 1
                y0 -= 1
                x0 += 1
                if x0<=7 and y0>=0 and board[x0][y0] == 0 and y0!=y-1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while x0+1<=7 and y0+1<=7 and self.board[x0+1][y0+1] == 1:
                    y0 += 1
                    x0 += 1
                y0 += 1
                x0 += 1
                if x0<=7 and y0<=7 and board[x0][y0] == 0 and y0!= y+1:
                    result.append((x0, y0))
        if player == 1:
            for x, y in self.blackPos:
                x0 = x
                y0 = y
                while x0-1 >= 0 and self.board[x0 - 1][y0] == -1:
                    x0 -= 1
                x0 -= 1
                if x0 >= 0 and board[x0][y0] == 0 and x0!=x-1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while y0-1 >= 0 and self.board[x0][y0 - 1] == -1:
                    y0 -= 1
                y0 -= 1
                if y0 >= 0 and board[x0][y0] == 0 and y0!=y-1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while x0+1 <= 7 and self.board[x0 + 1][y0] == -1:
                    x0 += 1
                x0 += 1
                if x0 <= 7 and board[x0][y0] == 0 and x0!=x+1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while y0+1 <= 7 and self.board[x0][y0 + 1] == -1:
                    y0 += 1
                y0 += 1
                if y0 <= 7 and board[x0][y0] == 0 and y0!=y+1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while x0-1 >= 0 and y0-1 >= 0 and self.board[x0 - 1][y0 - 1] == -1:
                    y0 -= 1
                    x0 -= 1
                y0 -= 1
                x0 -= 1
                if x0 >= 0 and y0 >= 0 and board[x0][y0] == 0 and y0!=y-1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while x0-1 >= 0 and y0+1 <= 7 and self.board[x0 - 1][y0 + 1] == -1:
                    y0 += 1
                    x0 -= 1
                y0 += 1
                x0 -= 1
                if x0 >= 0 and y0 <= 7 and board[x0][y0] == 0 and y0!=y+1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while x0+1 <= 7 and y0-1 >= 0 and self.board[x0 + 1][y0 - 1] == -1:
                    y0 -= 1
                    x0 += 1
                y0 -= 1
                x0 += 1
                if x0 <= 7 and y0 >= 0 and board[x0][y0] == 0 and y0!=y-1:
                    result.append((x0, y0))
                x0 = x
                y0 = y
                while x0+1 <= 7 and y0+1 <= 7 and self.board[x0 + 1][y0 + 1] == -1:
                    y0 += 1
                    x0 += 1
                y0 += 1
                x0 += 1
                if x0 <= 7 and y0 <= 7 and board[x0][y0] == 0 and y0!=y+1:
                    result.append((x0, y0))
        return list(set(result))

    def update(self, x, y, player):
        if player == -1:
            self.board[x][y] = -1
            # 向上
            x0, y0 = x - 1, y
            while x0 >= 0 and self.board[x0][y0] == 1:
                x0 -= 1
                if x0 >= 0 and self.board[x0][y0] == -1:
                    x0 += 1
                    while x0 != x:
                        self.board[x0][y0] = -1
                        x0 += 1
                    break

            # 向下
            x0, y0 = x + 1, y
            while x0 <= 7 and self.board[x0][y0] == 1:
                x0 += 1
                if x0 <= 7 and self.board[x0][y0] == -1:
                    x0 -= 1
                    while x0 != x:
                        self.board[x0][y0] = -1
                        x0 -= 1
                    break

            # 向左
            x0, y0 = x, y - 1
            while y0 >= 0 and self.board[x0][y0] == 1:
                y0 -= 1
                if y0 >= 0 and self.board[x0][y0] == -1:
                    y0 += 1
                    while y0 != y:
                        self.board[x0][y0] = -1
                        y0 += 1
                    break

            # 向右
            x0, y0 = x, y + 1
            while y0 <= 7 and self.board[x0][y0] == 1:
                y0 += 1
                if y0 <= 7 and self.board[x0][y0] == -1:
                    y0 -= 1
                    while y0 != y:
                        self.board[x0][y0] = -1
                        y0 -= 1
                    break

            # 左上
            x0, y0 = x - 1, y - 1
            while x0 >= 0 and y0 >= 0 and self.board[x0][y0] == 1:
                x0 -= 1
                y0 -= 1
                if x0 >= 0 and y0 >= 0 and self.board[x0][y0] == -1:
                    x0 += 1
                    y0 += 1
                    while x0 != x and y0 != y:
                        self.board[x0][y0] = -1
                        x0 += 1
                        y0 += 1
                    break

            # 右上
            x0, y0 = x - 1, y + 1
            while x0 >= 0 and y0 <= 7 and self.board[x0][y0] == 1:
                x0 -= 1
                y0 += 1
                if x0 >= 0 and y0 <= 7 and self.board[x0][y0] == -1:
                    x0 += 1
                    y0 -= 1
                    while x0 != x and y0 != y:
                        self.board[x0][y0] = -1
                        x0 += 1
                        y0 -= 1
                    break

            # 左下
            x0, y0 = x + 1, y - 1
            while x0 <= 7 and y0 >= 0 and self.board[x0][y0] == 1:
                x0 += 1
                y0 -= 1
                if x0 <= 7 and y0 >= 0 and self.board[x0][y0] == -1:
                    x0 -= 1
                    y0 += 1
                    while x0 != x and y0 != y:
                        self.board[x0][y0] = -1
                        x0 -= 1
                        y0 += 1
                    break

            # 右下
            x0, y0 = x + 1, y + 1
            while x0 <= 7 and y0 <= 7 and self.board[x0][y0] == 1:
                x0 += 1
                y0 += 1
                if x0 <= 7 and y0 <= 7 and self.board[x0][y0] == -1:
                    x0 -= 1
                    y0 -= 1
                    while x0 != x and y0 != y:
                        self.board[x0][y0] = -1
                        x0 -= 1
                        y0 -= 1
                    break

        elif player == 1:
            self.board[x][y] = 1
            # 向上
            x0, y0 = x - 1, y
            while x0 >= 0 and self.board[x0][y0] == -1:
                x0 -= 1
                if x0 >= 0 and self.board[x0][y0] == 1:
                    x0 += 1
                    while x0 != x:
                        self.board[x0][y0] = 1
                        x0 += 1
                    break

            # 向下
            x0, y0 = x + 1, y
            while x0 <= 7 and self.board[x0][y0] == -1:
                x0 += 1
                if x0 <= 7 and self.board[x0][y0] == 1:
                    x0 -= 1
                    while x0 != x:
                        self.board[x0][y0] = 1
                        x0 -= 1
                    break

            # 向左
            x0, y0 = x, y - 1
            while y0 >= 0 and self.board[x0][y0] == -1:
                y0 -= 1
                if y0 >= 0 and self.board[x0][y0] == 1:
                    y0 += 1
                    while y0 != y:
                        self.board[x0][y0] = 1
                        y0 += 1
                    break

            # 向右
            x0, y0 = x, y + 1
            while y0 <= 7 and self.board[x0][y0] == -1:
                y0 += 1
                if y0 <= 7 and self.board[x0][y0] == 1:
                    y0 -= 1
                    while y0 != y:
                        self.board[x0][y0] = 1
                        y0 -= 1
                    break

            # 左上
            x0, y0 = x - 1, y - 1
            while x0 >= 0 and y0 >= 0 and self.board[x0][y0] == -1:
                x0 -= 1
                y0 -= 1
                if x0 >= 0 and y0 >= 0 and self.board[x0][y0] == 1:
                    x0 += 1
                    y0 += 1
                    while x0 != x and y0 != y:
                        self.board[x0][y0] = 1
                        x0 += 1
                        y0 += 1
                    break

            # 右上
            x0, y0 = x - 1, y + 1
            while x0 >= 0 and y0 <= 7 and self.board[x0][y0] == -1:
                x0 -= 1
                y0 += 1
                if x0 >= 0 and y0 <= 7 and self.board[x0][y0] == 1:
                    x0 += 1
                    y0 -= 1
                    while x0 != x and y0 != y:
                        self.board[x0][y0] = 1
                        x0 += 1
                        y0 -= 1
                    break

            # 左下
            x0, y0 = x + 1, y - 1
            while x0 <= 7 and y0 >= 0 and self.board[x0][y0] == -1:
                x0 += 1
                y0 -= 1
                if x0 <= 7 and y0 >= 0 and self.board[x0][y0] == 1:
                    x0 -= 1
                    y0 += 1
                    while x0 != x and y0 != y:
                        self.board[x0][y0] = 1
                        x0 -= 1
                        y0 += 1
                    break

            # 右下
            x0, y0 = x + 1, y + 1
            while x0 <= 7 and y0 <= 7 and self.board[x0][y0] == -1:
                x0 += 1
                y0 += 1
                if x0 <= 7 and y0 <= 7 and self.board[x0][y0] == 1:
                    x0 -= 1
                    y0 -= 1
                    while x0 != x and y0 != y:
                        self.board[x0][y0] = 1
                        x0 -= 1
                        y0 -= 1
                    break
        newWhitePos = []
        newBlackPos = []
        whiteCnt = 0
        blackCnt = 0
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == -1:
                    newWhitePos.append((x, y))
                    whiteCnt += 1
                elif self.board[x][y] == 1:
                    newBlackPos.append((x, y))
                    blackCnt += 1
        self.numWhite = whiteCnt
        self.numBlack = blackCnt
        self.whitePos = newWhitePos
        self.blackPos = newBlackPos




def drawGame(board):
    for x in range(8):
        for y in range(8):
            if board[x][y] == -1:
                print("X ", end="")
            elif board[x][y] == 1:
                print("O ", end="")
            else:
                print("L ", end="")
        print("")


def getAction(nextPos):
    t = input(f"Legal:{nextPos}\nYour move:")
    x, y = map(int, t.split(", "))
    return x, y
