from collections import defaultdict, Counter
import random


def restore_list(slices):
    # Шаг 1: Найдем все уникальные числа и подсчитаем их частоты
    unique_numbers = set()
    frequency = Counter()

    for slc in slices:
        unique_numbers.update(slc)
        frequency.update(slc)

    # Шаг 2: Создадим граф порядка чисел
    before = defaultdict(set)
    after = defaultdict(set)

    for slc in slices:
        for i in range(2):
            after[slc[i]].add(slc[i + 1])
            before[slc[i + 1]].add(slc[i])

    # Шаг 3: Найдем возможные начала списка (числа, у которых нет предшественников)
    candidates = unique_numbers - {num for nums in before.values() for num in nums}

    # Если кандидатов несколько, выберем случайного
    if not candidates:
        candidates = unique_numbers
    current = random.choice(list(candidates))

    # Шаг 4: Восстановим исходный список
    result = []
    used = Counter()  # Для подсчета уже использованных чисел

    while current:
        result.append(current)
        used[current] += 1

        # Ищем возможных кандидатов для следующего числа
        next_numbers = after[current] - {num for num in result if used[num] >= frequency[num]}

        # Если несколько вариантов, выбираем случайно
        if next_numbers:
            current = random.choice(list(next_numbers))
        else:
            remaining_candidates = unique_numbers - set(result)
            if remaining_candidates:
                # Выбираем из оставшихся кандидатов, если список еще не завершен
                current = random.choice(list(remaining_candidates))
            else:
                current = None  # Завершение списка

    return result


# Пример с кортежами
reels_on_fire1 = [(80,80,80),(2,2,2),(5,5,20),(80,80,80),(5,5,4),(80,2,15),(20,6,4),(80,7,15),(6,15,2),
          (20,80,80),(6,6,2),(7,4,4),(2,2,5),(7,7,25),(7,80,6),(6,6,6),(7,2,6),(5,20,15),
          (5,7,4),(4,4,80),(4,7,5),(25,2,4),(2,6,6),(15,25,7),(5,80,7),(20,6,15),(6,15,25),
          (6,5,15),(5,5,5),(80,6,5),(15,5,25),(80,80,25),(15,4,6),(15,7,80),(15,15,20),(2,4,6),
          (2,4,80),(5,20,7),(2,2,2),(25,5,20),(15,7,20),(80,20,6),(5,2,7),(6,4,7),(2,20,5),
          (25,5,6)]
result = restore_list(reels_on_fire1)
print(result)
