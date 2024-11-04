import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Цвета
black = (0, 0, 0)
green = (0, 255, 0)

# Шрифты и символы
font = pygame.font.SysFont('courier', 20, bold=True)
symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890あいうえおカキクケコサシスセソ'


# Класс для создания колонки с символами
class SymbolColumn:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.symbols = [random.choice(symbols) for _ in range(20)]  # 20 символов в колонке

    def draw(self):
        # Рисуем символы в колонке
        for i, symbol in enumerate(self.symbols):
            symbol_surface = font.render(symbol, True, green)
            screen.blit(symbol_surface, (self.x, self.y + i * 20))
        # Двигаем колонку вниз
        self.y += self.speed
        # Если колонка вышла за экран, начинаем сверху
        if self.y > height:
            self.y = -len(self.symbols) * 20


# Создание колонок символов
columns = [SymbolColumn(x, random.randint(-height, 0), random.randint(2, 10)) for x in range(0, width, 20)]

# Главный игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Заполнение фона черным цветом
    screen.fill(black)

    # Отрисовка всех колонок
    for column in columns:
        column.draw()

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    pygame.time.Clock().tick(30)
