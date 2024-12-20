from collections import Counter

# Определяем рилы
reel1 = [5, 3, 6, 1, 2, 7, 3, 8, 1, 3, 8, 1, 0, 4, 5, 3, 6, 1, 2, 7, 3, 8, 1, 3, 8, 1, 0, 4, 5, 3, 6, 1, 2, 7, 3, 8, 1, 3, 8, 1, 1, 1, 2, 3, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
reel2 = [6, 1, 2, 0, 7, 3, 8, 0, 1, 4, 2, 0, 5, 3, 6, 1, 2, 0, 7, 3, 8, 0, 1, 4, 2, 0, 5, 3, 6, 1, 2, 0, 7, 3, 8, 0, 1, 4, 2, 0, 5, 3, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
reel3 = [2, 5, 0, 3, 6, 0, 1, 2, 0, 7, 3, 0, 8, 1, 0, 4, 2, 5, 0, 3, 6, 0, 1, 2, 0, 7, 3, 0, 8, 1, 0, 4, 2, 5, 0, 3, 6, 0, 1, 2, 0, 7, 3, 0, 8, 1, 0, 4, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Подсчёт количества каждого числа в каждом риле и общего количества
def count_numbers(reel):
    counts = Counter(reel)
    sorted_counts = dict(sorted(counts.items()))  # Сортируем по ключам
    total_count = sum(counts.values())
    return sorted_counts, total_count


reel1_counts, reel1_total = count_numbers(reel1)
reel2_counts, reel2_total = count_numbers(reel2)
reel3_counts, reel3_total = count_numbers(reel3)

# Вывод результатов
print("Рил 1 - Количество цифр:", reel1_counts, ", Общее количество цифр:", reel1_total)
print("Рил 2 - Количество цифр:", reel2_counts, ", Общее количество цифр:", reel2_total)
print("Рил 3 - Количество цифр:", reel3_counts, ", Общее количество цифр:", reel3_total)
