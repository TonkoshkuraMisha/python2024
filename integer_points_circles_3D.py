def count_integer_points_within_spheres(max_radius):
    result = {}

    for radius in range(1, max_radius + 1):
        count = 0
        radius_squared = radius ** 2

        # Проходим по всем точкам (x, y, z), которые могут попадать внутрь сферы радиуса radius
        for x in range(-radius, radius + 1):
            for y in range(-radius, radius + 1):
                for z in range(-radius, radius + 1):
                    if x ** 2 + y ** 2 + z ** 2 <= radius_squared:
                        count += 1

        result[radius] = count

    return result


# Пример использования:
max_radius = 100
points_within_spheres = count_integer_points_within_spheres(max_radius)
print(points_within_spheres)
