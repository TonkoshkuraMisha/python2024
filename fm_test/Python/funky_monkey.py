import random
from collections import defaultdict
import numpy as np
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

# Параметры
spins = int(1e7)
bet_per_spin = 1

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

# Счетчики выигрышей и статистика
total_winnings = 0
win_counts = defaultdict(int)
win_amounts = []

# Определяем шаг для прогресса
progress_step = spins // 10

# Симуляция вращений
for spin in range(spins):
    symbol1 = random.choice(reel1)
    symbol2 = random.choice(reel2)
    symbol3 = random.choice(reel3)
    combination = (symbol1, symbol2, symbol3)

    # Подсчёт выигрыша за комбинацию
    if combination in paytable:
        win = paytable[combination] * bet_per_spin
        total_winnings += win
        win_counts[combination] += 1
        win_amounts.append(win)
    else:
        win_amounts.append(0)

    # Вывод прогресса каждые 10%
    if (spin + 1) % progress_step == 0:
        progress = (spin + 1) * 100 // spins
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"{current_time}: {'*' * progress}{'-' * (100 - progress)} {progress}% Done.")

# Расчёт RTP и частоты выигрышей по комбинациям
total_bet = spins * bet_per_spin
overall_rtp = (total_winnings / total_bet) * 100
combination_rtp = {combo: (count * paytable[combo] * bet_per_spin / total_bet) * 100 for combo, count in
                   win_counts.items()}

# Расчёт распределения выигрышей по интервалам
intervals = [0, 30, 60, 120, 180, 240, 300, 600, 1200, 2500, 20000]
win_distribution = defaultdict(int)
for win in win_amounts:
    for i in range(len(intervals) - 1):
        if intervals[i] < int(win / bet_per_spin) <= intervals[i + 1]:
            win_distribution[f"{intervals[i] + 1}-{intervals[i + 1]}"] += 1
            break

# Волатильность и стандартное отклонение выигрышей
win_std = np.std(win_amounts)
volatility = win_std / bet_per_spin

# Вывод результатов
print(f"Общий выигрыш: {total_winnings}")
print(f"Общая ставка: {total_bet}")
print(f"Общее RTP: {overall_rtp:.2f}%\n")

print("RTP для каждой комбинации:")
for combo, rtp in sorted(combination_rtp.items()):
    print(f"{combo}: {rtp:.2f}%")

print(f"Частота выпадения комбинаций:")
for combo, frequency in sorted(win_counts.items()):
    print(f"{combo}: {frequency} per {spins} spins")

# Сортировка интервалов по первому числу
sorted_intervals = sorted(win_distribution.items(), key=lambda x: int(x[0].split('-')[0]))

print("\nРаспределение выигрышей по интервалам:")
for interval, count in win_distribution.items():
    print(f"{interval}: {count} раз")

print(f"\nСтандартное отклонение выигрышей: {win_std:.2f}")
print(f"Волатильность: {volatility:.2f}")
