import time
import random


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def measure_time(func, arr, target, iterations=10):
    total_time = 0
    for _ in range(iterations):
        start_time = time.time()
        result = func(arr, target)
        end_time = time.time()
        total_time += (end_time - start_time)
    return result, total_time / iterations


# Генерация большого списка данных
arr_size = 1000000000  # 1 миллиард
arr = list(range(arr_size))
target = random.randint(0, arr_size - 1)  # Целевое значение в пределах массива

# Измерение времени рекурсивного бинарного поиска
result_recursive, time_recursive = measure_time(lambda a, t: binary_search_recursive(a, t, 0, len(a) - 1), arr, target)

# Измерение времени итеративного бинарного поиска
result_iterative, time_iterative = measure_time(binary_search_iterative, arr, target)

# Вывод результатов
print(
    f"Рекурсивный подход: Элемент {target} найден в позиции {result_recursive}. Время выполнения: {time_recursive:.6f} секунд.")
print(
    f"Итеративный подход: Элемент {target} найден в позиции {result_iterative}. Время выполнения: {time_iterative:.6f} секунд.")
