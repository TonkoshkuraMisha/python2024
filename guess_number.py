import random


def guess_number_game():
    # Задаем случайное число от 1 до 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100. Попробуйте угадать его!")

    while True:
        # Запрашиваем у пользователя число
        try:
            guess = int(input("Введите ваше предположение: "))
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Слишком маленькое число. Попробуйте еще раз.")
        elif guess > number_to_guess:
            print("Слишком большое число. Попробуйте еще раз.")
        else:
            print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
            break


# Запускаем игру
if __name__ == "__main__":
    guess_number_game()
