import csv
import random
from collections import defaultdict
from datetime import datetime

# Данные
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

reel3 = [9, 8, 8, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 0,
         3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0]

# Таблица выплат
paytable = {
    (1, 1, 1): 60, (1, 1, 2): 30, (1, 1, 3): 30, (1, 2, 1): 30,
    (1, 2, 2): 30, (1, 2, 3): 30, (1, 3, 1): 30, (1, 3, 2): 30,
    (1, 3, 3): 30, (2, 1, 1): 30, (2, 1, 2): 30, (2, 1, 3): 30,
    (2, 2, 1): 30, (2, 2, 2): 120, (2, 2, 3): 30, (2, 3, 1): 30,
    (2, 3, 2): 30, (2, 3, 3): 30, (3, 1, 1): 30, (3, 1, 2): 30,
    (3, 1, 3): 30, (3, 2, 1): 30, (3, 2, 2): 30, (3, 2, 3): 30,
    (3, 3, 1): 30, (3, 3, 2): 30, (3, 3, 3): 180, (4, 4, 4): 240,
    (5, 5, 5): 300, (6, 6, 6): 600, (7, 7, 7): 1200, (8, 8, 8): 2500,
    (9, 9, 9): 20000
}

# Параметры
spins = int(1e6)  # для тестов можно сократить число
bet_per_spin = 5
save_interval = int(1e5)  # Интервал выгрузки данных
intervals = list(range(0, 10001, 1000))

# Счетчики выигрышей и статистика
total_winnings = 0
win_counts = defaultdict(int)
win_distribution = defaultdict(int)

# Симуляция вращений
for spin in range(spins):
    symbol1 = random.choice(reel1)
    symbol2 = random.choice(reel2)
    symbol3 = random.choice(reel3)
    combination = (symbol1, symbol2, symbol3)

    # Подсчёт выигрыша за комбинацию
    win = paytable.get(combination, 0) * bet_per_spin
    total_winnings += win
    win_counts[combination] += 1

    # Распределение выигрышей по интервалам
    interval_key = next((f"{intervals[i] + 1}-{intervals[i + 1]}" for i in range(len(intervals) - 1)
                         if intervals[i] < int(win / bet_per_spin) <= intervals[i + 1]), "0-0")
    win_distribution[interval_key] += 1

    # Вывод прогресса
    if (spin + 1) % save_interval == 0:
        progress = (spin + 1) * 100 // spins
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"{current_time}: {'*' * progress}{'-' * (100 - progress)} {progress}% Done.")

# Финальные расчёты и вывод результатов
total_bet = spins * bet_per_spin
overall_rtp = (total_winnings / total_bet) * 100
combination_rtp = {
    combo: (count * paytable[combo] * bet_per_spin / total_bet) * 100
    for combo, count in win_counts.items() if combo in paytable
}

# Вывод результатов
print(f"\nОбщий выигрыш: {total_winnings}")
print(f"Общая ставка: {total_bet}")
print(f"Общее RTP: {overall_rtp:.2f}%\n")

print("RTP для каждой комбинации:")
for combo, rtp in sorted(combination_rtp.items()):
    print(f"{combo}: {rtp:.2f}%")

print("\nЧастота выпадения комбинаций:")
for combo, frequency in sorted(win_counts.items()):
    print(f"{combo}: {frequency} раз за {spins} вращений")

# Сортировка интервалов по первому числу
sorted_intervals = sorted(win_distribution.items(), key=lambda x: int(x[0].split('-')[0]))

print("\nРаспределение выигрышей по интервалам:")
for interval, count in sorted_intervals:
    print(f"{interval}: {count} раз")

# Расчёт волатильности на основе накопленных данных
average_win = total_winnings / spins
win_variance = sum((paytable[combo] * bet_per_spin - average_win) ** 2 * freq
                   for combo, freq in win_counts.items() if combo in paytable) / spins
volatility = (win_variance ** 0.5) / bet_per_spin

print(f"\nСтандартное отклонение выигрышей: {volatility:.2f}")
print(f"Волатильность: {volatility:.2f}")

# Запись в CSV файл
with open('slot_simulation_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Дата", "Общий выигрыш", "Общая ставка", "Общее RTP", "Стандартное отклонение", "Волатильность"])
    writer.writerow(
        [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), total_winnings, total_bet, overall_rtp, volatility, volatility])

    writer.writerow(["Комбинация", "RTP (%)"])
    for combo, rtp in combination_rtp.items():
        writer.writerow([combo, rtp])

    writer.writerow(["Комбинация", "Частота выпадения"])
    for combo, frequency in win_counts.items():
        writer.writerow([combo, frequency])

    writer.writerow(["Интервал выигрышей", "Частота"])
    for interval, frequency in win_distribution.items():
        writer.writerow([interval, frequency])

print("Результаты сохранены в 'slot_simulation_results.csv'.")
