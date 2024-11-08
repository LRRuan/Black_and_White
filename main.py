from game import gameState, drawGame, getAction

# from optparse import OptionParser
# usageStr = """
#     USAGE:      python pacman.py <options>
#     EXAMPLES:   (1) python pacman.py
#                     - starts an interactive game
#                 (2) python pacman.py --layout smallClassic --zoom 2
#                 OR  python pacman.py -l smallClassic -z 2
#                     - starts an interactive game on a smaller board, zoomed in
#     """
# parser = OptionParser(usageStr)
#


game = gameState()

drawGame(game.board)

from Agents import AlphaBetaAgent

agentEnabled = True
if agentEnabled:
    alpha_beta_agent = AlphaBetaAgent()

while True:
    game.timeInc()
    player = game.getPlayer()
    board = game.getBoard()
    nextPos = game.getPlayPosition(player)
    #if agentEnable:     if player==-1...xy=...update draw break

    if nextPos == []:
        if game.numWhite+game.numBlack==64:
            print("WIN!")
            break
        else:
            continue

    if agentEnabled:
        if player == -1:
            x, y = alpha_beta_agent.getAction(game)
            game.update(x, y, -1)
            drawGame(game.board)
            print(x, y)
            continue
    x, y = getAction(nextPos)
    while (x, y) not in nextPos:
        print("Invalid move!")
        x, y = getAction(nextPos)
    if (x, y) in nextPos:
        game.update(x, y, player)
        drawGame(game.board)
        print("")




