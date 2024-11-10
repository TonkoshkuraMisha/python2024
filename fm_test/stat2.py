from collections import Counter, defaultdict
from itertools import product

# Определяем рилы
reel1 = [9, 8, 8, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4,
         3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0]

reel2 = [9, 8, 8, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4,
         3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0]

reel3 = [9, 8, 8, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4,
         3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0]
# Подсчёт количества каждого числа в каждом риле и общего количества
def count_numbers(reel):
    counts = Counter(reel)
    sorted_counts = dict(sorted(counts.items()))  # Сортируем по ключам
    total_count = sum(counts.values())
    return sorted_counts, total_count

reel1_counts, reel1_total = count_numbers(reel1)
reel2_counts, reel2_total = count_numbers(reel2)
reel3_counts, reel3_total = count_numbers(reel3)

# Частоты выпадения каждой цифры на каждом барабане
reel1_frequencies = {k: round(v / reel1_total, 4) for k, v in reel1_counts.items()}
reel2_frequencies = {k: round(v / reel2_total, 4) for k, v in reel2_counts.items()}
reel3_frequencies = {k: round(v / reel3_total, 4) for k, v in reel3_counts.items()}

# Подсчёт вероятностей для каждой комбинации из трёх барабанов с учётом перестановок
combination_probabilities = defaultdict(float)
for comb in product(reel1_frequencies.keys(), reel2_frequencies.keys(), reel3_frequencies.keys()):
    prob = reel1_frequencies[comb[0]] * reel2_frequencies[comb[1]] * reel3_frequencies[comb[2]]
    sorted_comb = tuple(sorted(comb))  # Сортируем комбинацию для объединения перестановок
    combination_probabilities[sorted_comb] += prob * 100  # Переводим вероятность в проценты

# Сортировка комбинаций по вероятности
sorted_combinations = dict(sorted(combination_probabilities.items(), key=lambda item: item[1], reverse=True))

# Вывод результатов
print("Рил 1 - Количество цифр:", reel1_counts, ", Общее количество цифр:", reel1_total)
print("Рил 2 - Количество цифр:", reel2_counts, ", Общее количество цифр:", reel2_total)
print("Рил 3 - Количество цифр:", reel3_counts, ", Общее количество цифр:", reel3_total)

print("\nЧастоты выпадения цифр на каждом барабане:")
print("Рил 1 частоты:", reel1_frequencies)
print("Рил 2 частоты:", reel2_frequencies)
print("Рил 3 частоты:", reel3_frequencies)

print("\nВероятности уникальных комбинаций из трёх барабанов (в процентах, от самой высокой к самой низкой):")
for comb, prob in sorted_combinations.items():
    print(f"Комбинация {comb}: вероятность {prob:.8f}%")
