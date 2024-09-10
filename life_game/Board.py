from Cell import Cell


class Board:
    def __init__(self, size):
        self.size = size
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                cell = Cell()
                row.append(cell)
            self.board.append(row)
        self.setNeighbors()
        self.lastClicked = None

    def getBoard(self):
        return self.board

    def getSize(self):
        return self.size

    def getCell(self, place):
        return self.board[place[0]][place[1]]

    def HandleClick(self, cell):
        if self.lastClicked is None:
            self.lastClicked = cell
        if self.lastClicked == cell:
            if not cell.getClicked():
                cell.handleClicked()
        else:
            self.lastClicked.notClicked()
            self.lastClicked = cell
            cell.handleClicked()

    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                cell = self.getCell((row, col))
                neighbors = self.getNeighbors((row, col))
                cell.setNeighbors(neighbors)

    def getNeighbors(self, place):
        neighbors = []
        for row in range(place[0] - 1, place[0] + 2):
            for col in range(place[1] - 1, place[1] + 2):
                if row == place[0] and col == place[1]:
                    continue
                if row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]:
                    continue
                neighbors.append(self.board[row][col])
        return neighbors

    def setNumAround(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                cell = self.getCell((row, col))
                cell.setNumAround()

    def resetBoard(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                cell = self.getCell((row, col))
                cell.setIsAlive(False)

