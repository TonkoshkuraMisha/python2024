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
symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890あいうえおカキクケコサシスセソ'

# Класс для создания колонки с символами
class SymbolColumn:
    def __init__(self, x, y, speed, font_size):
        self.x = x
        self.y = y
        self.speed = speed
        self.font_size = font_size
        self.symbols = [random.choice(symbols) for _ in range(20)]
        self.font = pygame.font.SysFont('courier', self.font_size, bold=True)
        self.static_symbol = random.choice([True, False])  # Некоторые символы статичны
        self.visibility_duration = random.randint(30, 200)  # Случайная продолжительность видимости
        self.visibility_timer = 0  # Счетчик для изменения состояния

    def draw(self):
        # Если символы статичны, не двигаем их
        if not self.static_symbol:
            self.y += self.speed

        # Перерисовываем символы
        for i, symbol in enumerate(self.symbols):
            if random.random() < 0.02:  # 2% вероятность смены символа
                self.symbols[i] = random.choice(symbols)
            # Если таймер вышел, символ исчезает и появляется в другом месте
            if self.visibility_timer > self.visibility_duration:
                self.y = random.randint(-100, 0)
                self.visibility_timer = 0
            else:
                self.visibility_timer += 1

            symbol_surface = self.font.render(symbol, True, green)
            screen.blit(symbol_surface, (self.x, self.y + i * self.font_size))

        # Если колонка вышла за экран, начинаем сверху
        if self.y > height:
            self.y = -len(self.symbols) * self.font_size

# Создание колонок символов с разными размерами и скоростями
columns = [
    SymbolColumn(x, random.randint(-height, 0), random.randint(2, 10), random.randint(15, 30))
    for x in range(0, width, 20)
]

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
