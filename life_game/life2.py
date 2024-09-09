import pygame
import numpy as np

# Инициализация Pygame
pygame.init()

# Константы
CELL_SIZE = 10
GRID_WIDTH = 80
GRID_HEIGHT = 60
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE
BACKGROUND_COLOR = (255, 255, 255)
LIVE_CELL_COLOR = (0, 255, 0)
DEAD_CELL_COLOR = (0, 0, 0)
LINE_COLOR = (0, 0, 0)
FPS = 10

# Устанавливаем размер экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Госпер Ган")

# Создаем поле игры
grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)

# Функция для отрисовки сетки
def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = LIVE_CELL_COLOR if grid[y, x] == 1 else DEAD_CELL_COLOR
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, LINE_COLOR, rect, 1)

# Функция для инициализации планерного ружья Госпера
def initialize_gosper_gun():
    pattern = [
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 0), (4, 0), (4, 1),
        (4, 2), (5, 1), (6, 2), (7, 1), (8, 1), (8, 2), (9, 1), (10, 1), (10, 2),
        (10, 3), (10, 4), (11, 1), (11, 2), (12, 3), (12, 4), (12, 5), (13, 0),
        (13, 1), (14, 0), (14, 1), (15, 1), (16, 0), (16, 1), (16, 2), (17, 1),
        (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1),
        (26, 1), (27, 1), (28, 1)
    ]
    for (x, y) in pattern:
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            grid[y, x] = 1

# Функция для обновления поля по правилам игры "Жизнь"
def update_grid():
    global grid
    new_grid = np.copy(grid)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = np.sum(grid[max(y-1, 0):min(y+2, GRID_HEIGHT), max(x-1, 0):min(x+2, GRID_WIDTH)]) - grid[y, x]
            if grid[y, x] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[y, x] = 0
            else:
                if neighbors == 3:
                    new_grid[y, x] = 1
    grid = new_grid

# Инициализация ружья Госпера
initialize_gosper_gun()

# Основной игровой цикл
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    draw_grid()
    update_grid()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
