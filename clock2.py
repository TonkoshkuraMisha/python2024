import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import requests


# Получение текущего времени через API
def get_time_from_api():
    try:
        response = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC")
        response.raise_for_status()
        data = response.json()
        utc_datetime = datetime.fromisoformat(data["datetime"][:-1])
        return utc_datetime.hour, utc_datetime.minute, utc_datetime.second
    except:
        now = datetime.now()
        return now.hour, now.minute, now.second


# Построение циферблата
def draw_clock(hour, minute, second):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')

    # Рисуем внешнюю окружность
    circle = plt.Circle((0, 0), 1.0, color="blue", fill=False, lw=2)
    ax.add_artist(circle)

    # Добавляем отметки минут
    for i in range(60):
        angle = 2 * np.pi * i / 60
        x1, y1 = 0.9 * np.cos(angle), 0.9 * np.sin(angle)
        x2, y2 = np.cos(angle), np.sin(angle)
        linewidth = 2 if i % 5 == 0 else 1
        ax.plot([x1, x2], [y1, y2], color="white", lw=linewidth)

    # Добавляем цифры
    for i in range(1, 13):
        angle = 2 * np.pi * (i / 12 - 0.25)
        x, y = 0.75 * np.cos(angle), 0.75 * np.sin(angle)
        ax.text(x, y, str(i), ha="center", va="center", fontsize=18, color="white", fontweight="bold")

    # Углы для стрелок
    second_angle = 2 * np.pi * (second / 60 - 0.25)
    minute_angle = 2 * np.pi * (minute / 60 - 0.25)
    hour_angle = 2 * np.pi * ((hour % 12 + minute / 60) / 12 - 0.25)

    # Рисуем стрелки
    ax.plot([0, 0.6 * np.cos(hour_angle)], [0, 0.6 * np.sin(hour_angle)], color="yellow", lw=8)  # Часовая
    ax.plot([0, 0.8 * np.cos(minute_angle)], [0, 0.8 * np.sin(minute_angle)], color="yellow", lw=4)  # Минутная
    ax.plot([0, 0.9 * np.cos(second_angle)], [0, 0.9 * np.sin(second_angle)], color="yellow", lw=2)  # Секундная

    plt.gca().set_facecolor('blue')  # Фон циферблата
    plt.show()


# Основная программа
hour, minute, second = get_time_from_api()
draw_clock(hour, minute, second)
