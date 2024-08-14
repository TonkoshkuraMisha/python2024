import random


def monte_carlo_pi(num_points):
    points_inside_circle = 0
    total_points = num_points

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x ** 2 + y ** 2

        if distance <= 1:
            points_inside_circle += 1

    pi_estimate = 4 * points_inside_circle / total_points
    return pi_estimate


# Пример использования
num_points = 1_000_000_000
estimated_pi = monte_carlo_pi(num_points)
print(f"Приближенное значение числа Пи с использованием {num_points} точек: {estimated_pi}")
