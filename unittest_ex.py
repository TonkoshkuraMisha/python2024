from math import sqrt


def square_eq_solver(a, b, c):
    """Нахождение корней квадратного уравнения"""
    if type(a) != type(b) != type(c) != int:
        raise ValueError
    rez = []
    d = b * b - 4 * a * c
    if d == 0:
        rez.append(-b / (2 * a))
    elif d < 0:
        return rez
    else:
        rez.append((-b + sqrt(d)) / (2 * a))
        rez.append((-b - sqrt(d)) / (2 * a))
    return rez

import unittest

class SquareEqSolverTestCase(unittest.TestCase):
    """ Дочерний класс от unittest.TestCase.
    Все его методы будут выполняться автоматически при вызове unittest.main() """

    def setUp(self):  # Этот метод будет выполняться перед КАЖДЫМ вызовом теста
        pass

    def test_no_root(self):
        # Этот и пять следующих методов - тесты, имена методов начинаются с test_
        res = square_eq_solver(10, 0, 2)
        self.assertEqual(len(res), 0)  # Это проверяемое условие, должно быть в каждом тесте

    def test_single_root(self):
        res = square_eq_solver(10, 0, 0)
        self.assertEqual(len(res), 1)

    def test_single_root_value(self):
        res = square_eq_solver(10, 0, 0)
        self.assertEqual(res, [0])

    def test_multiple_root(self):
        res = square_eq_solver(2, 5, -3)
        self.assertEqual(len(res), 2)

    def test_multiple_root_value(self):
        res = square_eq_solver(2, 5, -3)
        self.assertEqual(res, [0.5, -3])

    def test_unexpected_values(self):
        with self.assertRaises(ValueError):
            res = square_eq_solver(None, [], {})
            print(res)

    def tearDown(self):  # Этот метод будет выполняться после КАЖДОГО вызова теста
        pass


# ВАЖНО! Без этого условного оператора unittest.main() не будет корректно работать
if __name__ == '__main__':
    # Основная функция unittest. Будет выполнять все тесты дочерних классов unittest.TestCase
    unittest.main()
    """ Вместо функции unittest.main() можно использовать команду
    python -m unittest файл.py, она сделает то же самое.
    python -m unittest -v файл.py для подробного вывода """
