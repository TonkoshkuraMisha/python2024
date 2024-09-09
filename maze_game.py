import random


def maze_game():
    print("Добро пожаловать в лабиринт!")
    print("Вам нужно выбрать правильный путь, чтобы выбраться из лабиринта.")

    # Начальное состояние
    location = "start"

    while True:
        if location == "start":
            print("Вы находитесь на входе в лабиринт.")
            print("Вы видите три пути: влево (l), вправо (r) и вперед (f).")
            move = input("Куда вы хотите идти? ")
            if move == "l":
                location = "left_room"
            elif move == "r":
                location = "right_room"
            elif move == "f":
                location = "forward_room"
            else:
                print("Неизвестный выбор. Пожалуйста, введите 'l', 'r' или 'f'.")

        elif location == "left_room":
            print("Вы в комнате слева. Здесь вы видите два пути: назад (b) или вперед (f).")
            move = input("Куда вы хотите идти? ")
            if move == "f":
                if random.choice([True, False]):
                    print("Вы нашли выход из лабиринта!")
                    break
                else:
                    print("Вы наткнулись на стену. Пожалуйста, вернитесь назад.")
                    location = "start"
            elif move == "b":
                location = "start"
            else:
                print("Неизвестный выбор. Пожалуйста, введите 'f' или 'b'.")

        elif location == "right_room":
            print("Вы в комнате справа. Здесь есть два пути: назад (b) или в лабиринт (m).")
            move = input("Куда вы хотите идти? ")
            if move == "b":
                location = "start"
            elif move == "m":
                if random.choice([True, False]):
                    print("Вы нашли секретный проход и продолжаете путь.")
                    location = "forward_room"
                else:
                    print("Вы попали в ловушку. Вернитесь назад.")
                    location = "start"
            else:
                print("Неизвестный выбор. Пожалуйста, введите 'b' или 'm'.")

        elif location == "forward_room":
            print("Вы в комнате с несколькими дверями. Выберите путь: лево (l), право (r) или вперед (f).")
            move = input("Куда вы хотите идти? ")
            if move == "l":
                print("Вы вернулись в стартовую точку. Попробуйте другой путь.")
                location = "start"
            elif move == "r":
                print("Вы наткнулись на стену. Вернитесь назад.")
                location = "start"
            elif move == "f":
                print("Поздравляю! Вы нашли выход из лабиринта!")
                break
            else:
                print("Неизвестный выбор. Пожалуйста, введите 'l', 'r' или 'f'.")

        else:
            print("Что-то пошло не так. Пожалуйста, попробуйте снова.")
            location = "start"


# Запускаем игру
if __name__ == "__main__":
    maze_game()
