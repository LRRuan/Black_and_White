import copy


def raiseNotDefined():
    raise NotImplemented
from game import gameState

class Agent:
    """
    An agent must define a getAction method, but may also define the
    following methods which will be called if they exist:

    def registerInitialState(self, state): # inspects the starting state
    """

    def __init__(self, index=0, depth=3):
        self.index = index
        self.depth = depth

    def getAction(self, state):
        """
        The Agent will receive a GameState (from either {pacman, capture, sonar}.py) and
        must return an action from Directions.{North, South, East, West, Stop}
        """
        raiseNotDefined()



def betterEvaluationFunction(gs: gameState):
    board = gs.board
    score = 0
    score += gs.numWhite
    for x, y in gs.whitePos:
        both = 0
        if x == 0 or x == 7:
            score += 2
            both += 1
        if y == 0 or y == 7:
            score += 2
            both += 1
        if both == 2:
            score += 6
    for x, y in gs.blackPos:
        both = 0
        if x == 0 or x == 7:
            score -= 2
            both += 1
        if y == 0 or y == 7:
            score -= 2
            both += 1
        if both == 2:
            score -= 10
    return score

better = betterEvaluationFunction

class AlphaBetaAgent(Agent):
    def getAction(self, gameState: gameState):

        def max_value(gameState: gameState, depth: int, alpha, beta):
            actions = gameState.getPlayPosition(-1)
            if actions==[] or depth == self.depth:
                return better(gameState), (0, 0)

            v = -float('inf')
            move = (0, 0)

            for action in actions:
                # 获取该行动的后继状态
                newgs = copy.deepcopy(gameState)
                x, y = action
                newgs.update(x, y, -1)
                # 递归调用min_value
                v2, _ = min_value(newgs, depth, alpha, beta)
                if v2 > v:  # 如果当前行动的评估分数更高，则更新
                    v = v2
                    move = action
                    alpha = max(alpha, v)
                if v > beta:  # 关键错误，不能取等号 下界相等时还需要往下判断上界
                    return v, move
            return v, move

        def min_value(gameState: gameState, depth: int, alpha, beta):

            actions = gameState.getPlayPosition(1)
            if actions == [] or depth == self.depth:
                return better(gameState), (0, 0)

            v = float('inf')
            move = (0, 0)

            for action in actions:
                # 获取该行动的后继状态
                newgs = copy.deepcopy(gameState)
                x, y = action
                newgs.update(x, y, 1)
                v2, _ = max_value(newgs, depth + 1, alpha, beta)

                if v2 < v:  # 如果当前行动的评估分数更低，则更新
                    v = v2
                    move = action
                    beta = min(beta, v)
                if v < alpha:  # 关键错误，不能取等号
                    return v, move
            return v, move

        _, move = max_value(gameState, 0, -float('inf'), float('inf'))  # 初始深度设为0
        return move

