import pygame
import numpy as np

# Инициализация Pygame
pygame.init()

# Константы
CELL_SIZE = 15
GRID_WIDTH = 80
GRID_HEIGHT = 60
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE
BACKGROUND_COLOR = (255, 255, 255)
CELL_COLOR = (10, 140, 25)  # зеленый цвет
LINE_COLOR = (0, 0, 0)
FPS = 10

# Устанавливаем размер экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Жизнь")

# Создаем поле игры
grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)


# Функция для отрисовки сетки
def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BACKGROUND_COLOR, rect)
            if grid[y, x] == 1:
                pygame.draw.rect(screen, CELL_COLOR, rect)
            pygame.draw.rect(screen, LINE_COLOR, rect, 1)


# Функция для обновления поля по правилам игры "Жизнь"
def update_grid():
    global grid
    new_grid = np.copy(grid)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = np.sum(grid[max(y - 1, 0):min(y + 2, GRID_HEIGHT), max(x - 1, 0):min(x + 2, GRID_WIDTH)]) - \
                        grid[y, x]
            if grid[y, x] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[y, x] = 0
            else:
                if neighbors == 3:
                    new_grid[y, x] = 1
    grid = new_grid


# Задайте координаты кастомной фигуры здесь
custom_shape = [(30, 29), (31, 28), (31, 30), (32, 29)]

# Инициализация кастомной фигуры в сетке
for (x, y) in custom_shape:
    if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
        grid[y, x] = 1

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
