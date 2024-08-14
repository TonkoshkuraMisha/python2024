import random


def monte_carlo_circle_area(num_points):
    points_inside_circle = 0
    total_points = num_points

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x ** 2 + y ** 2

        if distance <= 1:
            points_inside_circle += 1

    circle_area_estimate = points_inside_circle / total_points * 4
    return circle_area_estimate


# Пример использования
num_points = 1000000
estimated_area = monte_carlo_circle_area(num_points)
print(f"Приближенная площадь круга с использованием {num_points} точек: {estimated_area}")
