def print_board(board):
    """Функция для печати доски Sudoku"""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


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


def main():
    # Пример доски Sudoku, где 0 представляет пустые клетки
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Исходная доска Sudoku:")
    print_board(board)

    if solve_sudoku(board):
        print("\nРешенная доска Sudoku:")
        print_board(board)
    else:
        print("\nНет решения для данной доски Sudoku.")


if __name__ == "__main__":
    main()
