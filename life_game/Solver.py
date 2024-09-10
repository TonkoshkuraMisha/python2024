class Solver:
    def __init__(self, board):
        self.board = board

    def nextGen(self):
        self.board.setNumAround()
        for row in range(self.board.size[0]):
            for col in range(self.board.size[1]):
                cell = self.board.getCell((row, col))
                around = cell.getNumAround()
                if (around == 2 or around == 3) and cell.getIsAlive():
                    cell.setIsAlive(True)
                if around == 3 and (not cell.getIsAlive()):
                    cell.setIsAlive(True)
                if (around < 2 or around > 3) and cell.getIsAlive():
                    cell.setIsAlive(False)

