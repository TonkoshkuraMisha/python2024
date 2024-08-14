import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle


def count_integer_points_within_sphere(radius):
    count = 0
    radius_squared = radius ** 2
    points = []

    # Проходим по всем точкам (x, y, z), которые могут попадать внутрь сферы радиуса radius
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            for z in range(-radius, radius + 1):
                if x ** 2 + y ** 2 + z ** 2 <= radius_squared:
                    points.append((x, y, z))
                    count += 1

    return count, points


def visualize_and_save_sphere(radius, output_folder='sphere_plots'):
    # Создаем папку, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    count, points = count_integer_points_within_sphere(radius)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Добавляем точки
    points = np.array(points)
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=10, color='blue')

    # Добавляем сферу
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color='red', alpha=0.3, edgecolor='k', linewidth=0.5)

    ax.set_title(f"Points within Sphere of Radius {radius} (Count: {count})")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Сохраняем изображение в папку
    filepath = os.path.join(output_folder, f'sphere_radius_{radius}.png')
    plt.savefig(filepath)
    plt.close()


# Пример использования:
initial_radius = 3
visualize_and_save_sphere(initial_radius)
