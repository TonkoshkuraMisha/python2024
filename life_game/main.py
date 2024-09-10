from Game import Game
from Board import Board

# size of game board in cells
size = (50, 50)
# creating board
board = Board(size)
# screen size
screenSize = (800, 700)
game = Game(board, screenSize)
game.run()
