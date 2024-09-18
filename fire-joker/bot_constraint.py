from constraint import Problem, AllDifferentConstraint


def restore_list_with_constraints(slices):
    # Найдем все уникальные числа
    unique_numbers = set()
    for slc in slices:
        unique_numbers.update(slc)

    # Создаем задачу
    problem = Problem()

    # Добавляем переменные
    problem.addVariables(list(unique_numbers), range(len(unique_numbers)))

    # Добавляем ограничения на порядок следования чисел в слайсах
    for slc in slices:
        problem.addConstraint(lambda x, y: x < y, (slc[0], slc[1]))
        problem.addConstraint(lambda x, y: x < y, (slc[1], slc[2]))

    # Решаем задачу
    solution = problem.getSolutions()

    if solution:
        # Преобразуем решение в список, отсортировав по значениям переменных
        ordered_solution = sorted(solution[0], key=solution[0].get)
        return ordered_solution
    else:
        return None


# Пример с кортежами
reels1 = [(80,15,2),(4,6,20),(2,5,20),(5,15,7),(2,2,7),(2,7,7),(25,25,25),(4,2,2),(80,6,2),
          (20,2,4),(80,20,6),(4,4,4),(15,6,4),(80,80,80),(80,2,15),(80,25,2),(2,6,6),(15,6,25),
          (20,7,7),(2,2,2)]
result = restore_list_with_constraints(reels1)
print(result)
