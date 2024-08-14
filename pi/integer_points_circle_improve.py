import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def count_integer_points_within_circle(radius):
    count = 0
    radius_squared = radius ** 2
    points = []

    # Проходим по всем точкам (x, y), которые могут попадать внутрь окружности радиуса radius
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            if x ** 2 + y ** 2 <= radius_squared:
                points.append((x, y))
                count += 1

    return count, points


def visualize_and_save_circle(radius, output_folder='circle_plots'):
    # Создаем папку, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    count, points = count_integer_points_within_circle(radius)

    plt.figure(figsize=(6, 6))
    ax = plt.gca()

    # Добавляем точки
    plt.scatter([x for x, y in points], [y for x, y in points], s=10, color='blue')

    # Добавляем окружность
    circle = Circle((0, 0), radius, color='red', fill=False, linestyle='--')
    ax.add_patch(circle)

    plt.title(f"Points within Circle of Radius {radius} (Count: {count})")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)

    # Сохраняем изображение в папку
    filepath = os.path.join(output_folder, f'circle_radius_{radius}.png')
    plt.savefig(filepath)
    plt.close()


# Пример использования:
initial_radius = 10
visualize_and_save_circle(initial_radius)
