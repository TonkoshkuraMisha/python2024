import random
import time


def find_max_non_increasing_subsequence(nums):
    if not nums:
        return []

    n = len(nums)
    lengths = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] <= nums[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                prev[i] = j

    max_length = max(lengths)
    index = lengths.index(max_length)

    subsequence = []
    while index != -1:
        subsequence.append(nums[index])
        index = prev[index]

    return subsequence[::-1]


# Генерация большой последовательности
def generate_large_sequence(size):
    return [random.randint(1, 10000) for _ in range(size)]


# Основная часть программы
if __name__ == "__main__":
    # Генерация последовательности из 10000 чисел
    nums = generate_large_sequence(10000)

    start_time = time.time()
    result = find_max_non_increasing_subsequence(nums)
    end_time = time.time()

    print(f"Наибольшая невозрастающая подпоследовательность имеет длину {len(result)}.")
    print(f"Самая большая невозрастающая подпоследовательность: {result}")
    print(f"Время выполнения: {end_time - start_time:.2f} секунд.")
