import time
import random


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time


# Генерация случайного списка для сортировки
arr = [random.randint(0, 1000000) for _ in range(1000000)]
arr_copy = arr.copy()

# Измеряем время выполнения собственной сортировки
time_custom = measure_time(lambda x: quick_sort(x, 0, len(x) - 1), arr)

# Измеряем время выполнения встроенной сортировки
time_builtin = measure_time(sorted, arr_copy)

print("Время выполнения собственной сортировки:", time_custom)
print("Время выполнения встроенной сортировки:", time_builtin)

# Проверяем корректность собственной сортировки
assert arr == sorted(arr_copy), "Собственная сортировка выполнена неверно!"
