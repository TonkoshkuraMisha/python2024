import numpy as np
import matplotlib.pyplot as plt
import time
import os


def monte_carlo_pi(num_points):
    # Генерация случайных точек внутри квадрата со стороной 2
    x = np.random.uniform(-1, 1, num_points)
    y = np.random.uniform(-1, 1, num_points)

    # Определение расстояний от точек до центра (0,0)
    distances = x ** 2 + y ** 2

    # Подсчет количества точек внутри круга радиусом 1
    inside_circle = distances <= 1

    # Оценка числа π
    pi_estimate = 4 * np.sum(inside_circle) / num_points

    return pi_estimate, x, y, inside_circle


def plot_results(x, y, inside_circle, output_folder='plots'):
    # Создаем папку, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    plt.figure(figsize=(8, 8))
    plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label='Inside Circle')
    plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Outside Circle')

    # Настройка границ графика
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # Добавление круга на график
    circle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
    plt.gca().add_patch(circle)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Monte Carlo Simulation for Estimating Pi')
    plt.legend()
    plt.grid(True)

    # Сохранение изображения в папку
    filepath = os.path.join(output_folder, f'monte_carlo_pi_plot_{num_points}.png')
    plt.savefig(filepath)
    plt.close()


# Пример использования:
num_points = 10000

# Замер времени выполнения
start_time = time.time()
pi_estimate, x, y, inside_circle = monte_carlo_pi(num_points)
end_time = time.time()

# Вывод результатов
print(f"Estimated value of π: {pi_estimate}")
print(f"Time taken: {end_time - start_time:.4f} seconds")

# Построение и сохранение графика
plot_results(x, y, inside_circle)
