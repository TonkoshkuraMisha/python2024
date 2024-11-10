import random
import settings
from collections import defaultdict
import numpy as np
from datetime import datetime

# Загружаем настройки
spins = int(settings.spins)
bet_per_spin = settings.bet_per_spin
reel1, reel2, reel3 = settings.reel1, settings.reel2, settings.reel3
paytable = settings.paytable

# Переменные для статистики
total_payout = 0
win_distribution = defaultdict(int)
win_counts = defaultdict(int)
win_intervals = defaultdict(list)
jackpot_rtp = 0
game_rtp = 0
spin_outcomes = []

# Считаем интервал между выигрышами для волатильности
last_win_spin = -1

# Определяем шаг для прогресса
progress_step = spins // 10

# Запуск симуляции спинов
for spin in range(spins):
    symbol1 = random.choice(reel1)
    symbol2 = random.choice(reel2)
    symbol3 = random.choice(reel3)

    # Полученная комбинация символов
    combination = [symbol1, symbol2, symbol3]

    # Проверка на выигрышную комбинацию
    if tuple(combination) in paytable:
        payout = paytable[tuple(combination)]
        total_payout += payout
        win_distribution[tuple(combination)] += payout
        win_counts[tuple(combination)] += 1

        # Джекпот отдельно
        if combination == [9, 9, 9]:
            jackpot_rtp += payout / spins

        # Вычисление интервалов выигрышей
        if last_win_spin != -1:
            interval = spin - last_win_spin
            win_intervals[tuple(combination)].append(interval)
        last_win_spin = spin

    spin_outcomes.append(payout if tuple(combination) in paytable else 0)

    # Вывод прогресса каждые 10%
    if (spin + 1) % progress_step == 0:
        progress = (spin + 1) * 100 // spins
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"{current_time}: {'*' * progress}{'-' * (100 - progress)} {progress}% Done.")

print(f"Идёт подготовка статистики...")

# Общий RTP игры (включая все выигрыши)
game_rtp = (total_payout / (spins * bet_per_spin)) * 100

# Частота выигрышей
win_frequencies = {k: f"{(v / spins) * 100:.5f}" for k, v in win_counts.items()}


# Распределение выигрыша по символам и интервалам
interval_means = {k: f"{np.mean(v):.5f}" if v else "0.00000" for k, v in win_intervals.items()}
interval_stds = {k: f"{np.std(v):.5f}" if v else "0.00000" for k, v in win_intervals.items()}


# Стандартное отклонение по выигрышам и волатильность
volatility = np.std(spin_outcomes)
std_deviation = np.std(
    [paytable.get(tuple([random.choice(reel1), random.choice(reel2), random.choice(reel3)]), 0) for _ in range(spins)])

# Результаты
print(f"Общий RTP: {game_rtp:.2f}%")
print(f"RTP Джекпота: {jackpot_rtp * 100:.2f}%")
print("Частоты выигрышей по комбинациям:", win_frequencies)
print("Распределение выигрышей по символам:", win_distribution)
print("Средние интервалы между выигрышами по комбинациям:", interval_means)
print("Стандартные отклонения интервалов выигрышей по комбинациям:", interval_stds)
print(f"Волатильность: {volatility:.2f}")
print(f"Стандартное отклонение выигрышей: {std_deviation:.2f}")
