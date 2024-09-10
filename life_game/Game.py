import pygame
from Solver import Solver
from time import sleep


class Game:
    def __init__(self, board, screenSize):
        self.board = board
        pygame.init()
        self.screenSize = screenSize
        self.screen = pygame.display.set_mode(self.screenSize)
        self.cellSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.liveImg = pygame.image.load('live.png')
        self.deadImg = pygame.image.load('dead.png')
        self.liveImg = pygame.transform.scale(self.liveImg, self.cellSize)
        self.deadImg = pygame.transform.scale(self.deadImg, self.cellSize)
        self.solver = Solver(self.board)

    # Main run function

    def run(self):
        running = True
        start = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # If left mouse pressed - change live/dead cell on board
                if pygame.mouse.get_pressed(num_buttons=3)[0] == 1:
                    self.handleClick(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        # prevent multiple clicks on same cell
                        self.board.lastClicked.notClicked()
                if event.type == pygame.KEYDOWN:
                    # 'Space' key starts/stops game
                    if event.key == pygame.K_SPACE:
                        start = not start
                    # 'R' key reset board 
                    if event.key == pygame.K_r:
                        self.board.resetBoard()
            if start:
                self.solver.nextGen()
                sleep(0.05)

            self.draw()
            pygame.display.flip()
        pygame.quit()
    
    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                cell = self.board.getCell((row, col))

                if cell.getIsAlive():
                    image = self.liveImg
                else:
                    image = self.deadImg
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.cellSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.cellSize[1]

    def handleClick(self, pos):
        index = pos[1] // self.cellSize[1], pos[0] // self.cellSize[0]
        cell = self.board.getCell(index)
        self.board.HandleClick(cell)
