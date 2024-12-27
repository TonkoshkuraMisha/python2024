import pygame
import datetime
import math
import requests

# Настройки экрана
WIDTH, HEIGHT = 600, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 250

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Аналоговые часы")

# Цвета
BLUE = (0, 0, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 223, 0)


# Функция получения времени
def get_current_time():
    # Можно заменить API запроса на более точный
    now = datetime.datetime.now()
    return now.hour, now.minute, now.second


# Функция рисования стрелки
def draw_hand(screen, angle, length, color, width):
    x = CENTER[0] + length * math.cos(angle)
    y = CENTER[1] - length * math.sin(angle)
    pygame.draw.line(screen, color, CENTER, (x, y), width)


# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(BLUE)

    # Рисование окружности часов
    pygame.draw.circle(screen, WHITE, CENTER, RADIUS, 5)

    # Рисование меток
    for i in range(12):
        angle = math.radians(360 / 12 * i)
        x = CENTER[0] + (RADIUS - 20) * math.cos(angle)
        y = CENTER[1] - (RADIUS - 20) * math.sin(angle)
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)

    # Получение текущего времени
    hour, minute, second = get_current_time()

    # Углы для каждой стрелки
    second_angle = math.radians((360 / 60) * second - 90)
    minute_angle = math.radians((360 / 60) * minute - 90)
    hour_angle = math.radians((360 / 12) * (hour % 12) - 90 + (30 * minute / 60))

    # Рисование стрелок
    draw_hand(screen, hour_angle, RADIUS * 0.5, YELLOW, 8)
    draw_hand(screen, minute_angle, RADIUS * 0.7, WHITE, 5)
    draw_hand(screen, second_angle, RADIUS * 0.9, WHITE, 2)

    # Обновление экрана
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
