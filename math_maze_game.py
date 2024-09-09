import random


def generate_problem():
    """Генерирует случайное математическое уравнение"""
    operators = ['+', '-', '*', '/']
    op = random.choice(operators)

    if op == '/':
        # Убедимся, что делитель не равен нулю
        num1 = random.randint(1, 100)
        num2 = random.randint(1, num1)
    else:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

    problem = f"{num1} {op} {num2}"
    answer = eval(problem)
    return problem, answer


def math_maze_game():
    print("Добро пожаловать в математический лабиринт!")
    print("Вам нужно решать математические задачи, чтобы продвигаться по уровням и найти выход.")

    level = 1
    while True:
        print(f"\nУровень {level}")

        problem, answer = generate_problem()
        print(f"Решите уравнение: {problem}")

        try:
            user_answer = float(input("Ваш ответ: "))
            if abs(user_answer - answer) < 1e-5:  # Учитываем погрешность для делений
                print("Правильно! Вы переходите на следующий уровень.")
                level += 1
                if level > 5:
                    print("Поздравляю! Вы нашли выход из лабиринта!")
                    break
            else:
                print("Неправильно. Попробуйте еще раз.")
        except ValueError:
            print("Пожалуйста, введите корректный числовой ответ.")


# Запускаем игру
if __name__ == "__main__":
    math_maze_game()
