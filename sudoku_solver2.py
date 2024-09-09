import random


def print_board(board):
    """Функция для печати доски Sudoku с разделением на блоки"""

    def print_row(row):
        """Функция для печати строки с разделением на блоки"""
        row_display = " ".join(f"{num:2}" if num != 0 else " ." for num in row[:3]) + " | " \
                      + " ".join(f"{num:2}" if num != 0 else " ." for num in row[3:6]) + " | " \
                      + " ".join(f"{num:2}" if num != 0 else " ." for num in row[6:])
        return row_display

    print("-" * 31)  # Широкая разделительная линия для визуального выделения
    for i, row in enumerate(board):
        if i % 3 == 0 and i > 0:
            print("-" * 31)  # Разделительная линия между блоками
        print(print_row(row))
    print("-" * 31)  # Широкая разделительная линия для завершения


def is_valid(board, row, col, num):
    """Функция проверки, является ли число допустимым для данной ячейки"""
    # Проверка строки
    if num in board[row]:
        return False

    # Проверка столбца
    if num in [board[i][col] for i in range(9)]:
        return False

    # Проверка 3x3 квадрата
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    """Функция для решения Sudoku с использованием рекурсии"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def generate_complete_board():
    """Генерация полностью решенной доски Sudoku"""
    board = [[0] * 9 for _ in range(9)]

    def fill_board():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for num in numbers:
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve_sudoku(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    fill_board()
    return board


def generate_starting_board(completed_board, empty_cells=40):
    """Генерация стартовой доски Sudoku из полностью решенной доски"""
    board = [row[:] for row in completed_board]
    cells_to_remove = empty_cells
    while cells_to_remove > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            cells_to_remove -= 1
    return board


def main():
    completed_board = generate_complete_board()
    starting_board = generate_starting_board(completed_board, empty_cells=40)

    print("Исходная доска Sudoku:")
    print_board(starting_board)

    if solve_sudoku(starting_board):
        print("\nРешенная доска Sudoku:")
        print_board(starting_board)
    else:
        print("\nНет решения для данной доски Sudoku.")


if __name__ == "__main__":
    main()
