import random
from collections import defaultdict

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


def main():
    spins = int(1e8)
    bet_per_spin = 2  # Множитель ставки
    total_winnings = 0
    win_counts = defaultdict(int)
    individual_wins = defaultdict(int)

    # Симуляция вращений
    for _ in range(spins):
        symbol1 = random.choice(reel1)
        symbol2 = random.choice(reel2)
        symbol3 = random.choice(reel3)
        combination = (symbol1, symbol2, symbol3)

        if combination in paytable:
            win = paytable[combination] * bet_per_spin  # Учитываем ставку
            total_winnings += win
            win_counts[combination] += 1
            individual_wins[symbol1] += win

    # Расчёт RTP
    total_bet = spins * bet_per_spin
    overall_rtp = (total_winnings / total_bet) * 100

    # Расчёт RTP для каждой комбинации
    combination_rtp = {combo: (count * paytable[combo] * bet_per_spin / total_bet) * 100
                       for combo, count in win_counts.items()}

    # Вывод результатов
    print(f"Общий выигрыш: {total_winnings}")
    print(f"Общая ставка: {total_bet}")
    print(f"Общее RTP: {overall_rtp:.2f}%\n")

    print("RTP для каждой комбинации:")
    for combo, rtp in combination_rtp.items():
        print(f"{combo}: {rtp:.2f}%")

    print("\nВыигрыши по отдельным символам:")
    for symbol, total_win in individual_wins.items():
        print(f"Символ {symbol}: {total_win}")


if __name__ == "__main__":
    main()
