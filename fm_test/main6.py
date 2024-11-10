from collections import defaultdict
from scipy.stats import rv_discrete
import numpy as np

# Данные
reel1 = [9, 8, 8, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4,
         3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

reel2 = [9, 8, 8, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4,
         3, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

reel3 = [9, 8, 8, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4,
         3, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Параметры
spins = int(1e6)
bet_per_spin = 5

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

# Создание случайного распределения для рилов
reel1_dist = rv_discrete(values=(range(len(reel1)), [1 / len(reel1)] * len(reel1)))
reel2_dist = rv_discrete(values=(range(len(reel2)), [1 / len(reel2)] * len(reel2)))
reel3_dist = rv_discrete(values=(range(len(reel3)), [1 / len(reel3)] * len(reel3)))

# Счетчики выигрышей и статистика
total_winnings = 0
win_counts = defaultdict(int)
individual_wins = defaultdict(int)
win_amounts = []

# Симуляция вращений
for _ in range(spins):
    symbol1 = reel1[reel1_dist.rvs()]
    symbol2 = reel2[reel2_dist.rvs()]
    symbol3 = reel3[reel3_dist.rvs()]
    combination = (symbol1, symbol2, symbol3)

    # Подсчёт выигрыша за комбинацию
    if combination in paytable:
        win = paytable[combination] * bet_per_spin
        total_winnings += win
        win_counts[combination] += 1
        individual_wins[symbol1] += win
        win_amounts.append(win)


# Расчёт RTP и частоты выигрышей
total_bet = spins * bet_per_spin
overall_rtp = (total_winnings / total_bet) * 100
combination_rtp = {combo: (count * paytable[combo] * bet_per_spin / total_bet) * 100 for combo, count in
                   win_counts.items()}
symbol_frequencies = {symbol: count / spins * 100 for symbol, count in individual_wins.items()}

# Расчёт распределения выигрышей по интервалам
intervals = [0, 30 * bet_per_spin + 1, 60 * bet_per_spin + 1, 120 * bet_per_spin + 1, 180 * bet_per_spin + 1,
             240 * bet_per_spin + 1, 300 * bet_per_spin + 1, 600 * bet_per_spin + 1, 1200 * bet_per_spin + 1,
             2500 * bet_per_spin + 1, 20000 * bet_per_spin + 1]
win_distribution = defaultdict(int)
for win in win_amounts:
    for i in range(len(intervals) - 1):
        if intervals[i] <= win < intervals[i + 1]:
            win_distribution[f"{intervals[i]}-{intervals[i + 1] - 1}"] += 1
            break

# Волатильность и стандартное отклонение выигрышей
win_std = np.std(win_amounts)
volatility = win_std / bet_per_spin

# Вывод результатов
print(f"Общий выигрыш: {total_winnings}")
print(f"Общая ставка: {total_bet}")
print(f"Общее RTP: {overall_rtp:.2f}%\n")

print("RTP для каждой комбинации:")
for combo, rtp in combination_rtp.items():
    print(f"{combo}: {rtp:.2f}%")

print("\nЧастота выигрышей по символам:")
for symbol, freq in symbol_frequencies.items():
    print(f"Символ {symbol}: {freq:.2f}%")

print("\nРаспределение выигрышей по интервалам:")
for interval, count in win_distribution.items():
    print(f"{interval}: {count} раз")

print(f"\nВолатильность игры: {volatility:.2f}")
print(f"Стандартное отклонение выигрышей: {win_std:.2f}")
