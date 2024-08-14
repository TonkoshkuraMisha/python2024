import random
import time


def find_max_non_increasing_subsequence_with_limit(nums, k):
    n = len(nums)

    if n == 0:
        return [], 0

    # Создаем список для хранения длин наибольших невозрастающих подпоследовательностей
    lengths = [1] * n
    prev = [-1] * n  # Для восстановления подпоследовательности

    # Заполняем список длин
    for i in range(1, n):
        for j in range(i):
            if nums[i] <= nums[j] and (nums[j] - nums[i]) <= k:
                if lengths[i] < lengths[j] + 1:
                    lengths[i] = lengths[j] + 1
                    prev[i] = j

    # Находим максимальную длину подпоследовательности
    max_length = max(lengths)
    index = lengths.index(max_length)

    # Восстанавливаем саму подпоследовательность
    subsequence = []
    while index != -1:
        subsequence.append(nums[index])
        index = prev[index]

    return subsequence[::-1], max_length


# Генерация длинного списка чисел
def generate_large_sequence(size, max_value):
    return [random.randint(1, max_value) for _ in range(size)]


# Параметры
sequence_size = 1000  # Размер списка
max_value = 100  # Максимальное значение в списке
k = 10  # Ограничение на разницу

# Генерация случайного списка чисел
nums = generate_large_sequence(sequence_size, max_value)

# Измерение времени выполнения
start_time = time.time()
result, length = find_max_non_increasing_subsequence_with_limit(nums, k)
end_time = time.time()

# Вывод результатов
print(f"Наибольшая невозрастающая подпоследовательность с разницей не более {k}:", result)
print(f"Длина подпоследовательности: {length}")
print(f"Время выполнения: {end_time - start_time:.2f} секунд")
