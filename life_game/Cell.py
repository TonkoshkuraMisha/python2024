class Cell:
    def __init__(self):
        self.isAlive = False
        self.clicked = False
        self.around = 0
        self.neighbors = []

    def setIsAlive(self, isAlive):
        self.isAlive = isAlive

    def getIsAlive(self):
        return self.isAlive

    def getClicked(self):
        return self.clicked

    def getNumAround(self):
        return self.around

    def handleClicked(self):
        self.isAlive = not self.isAlive
        self.clicked = True

    def setNumAround(self):
        num = 0
        for cell in self.neighbors:
            if cell.getIsAlive():
                num = num + 1
        self.around = num

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors

    def getNeighbors(self):
        return self.neighbors

    def notClicked(self):
        self.clicked = False
