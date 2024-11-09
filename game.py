
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
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        opponent = 1 if player == -1 else -1
        positions = self.whitePos if player == -1 else self.blackPos
        result = []

        for x, y in positions:
            for dx, dy in directions:
                x0, y0 = x + dx, y + dy
                has_opponent_in_between = False
                while 0 <= x0 < 8 and 0 <= y0 < 8 and self.board[x0][y0] == opponent:
                    x0 += dx
                    y0 += dy
                    has_opponent_in_between = True
                if 0 <= x0 < 8 and 0 <= y0 < 8 and self.board[x0][y0] == 0 and has_opponent_in_between:
                    result.append((x0, y0))

        return list(set(result))

    def update(self, x, y, player):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        opponent = 1 if player == -1 else -1
        self.board[x][y] = player

        for dx, dy in directions:
            x0, y0 = x + dx, y + dy
            pieces_to_flip = []
            while 0 <= x0 < 8 and 0 <= y0 < 8 and self.board[x0][y0] == opponent:
                pieces_to_flip.append((x0, y0))
                x0 += dx
                y0 += dy
            if 0 <= x0 < 8 and 0 <= y0 < 8 and self.board[x0][y0] == player:
                for flip_x, flip_y in pieces_to_flip:
                    self.board[flip_x][flip_y] = player

        self.update_positions_and_counts()

    def update_positions_and_counts(self):
        self.whitePos, self.blackPos = [], []
        self.numWhite, self.numBlack = 0, 0

        for x in range(8):
            for y in range(8):
                if self.board[x][y] == -1:
                    self.whitePos.append((x, y))
                    self.numWhite += 1
                elif self.board[x][y] == 1:
                    self.blackPos.append((x, y))
                    self.numBlack += 1



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
