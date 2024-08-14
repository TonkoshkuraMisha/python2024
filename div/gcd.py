def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    import sys

    if len(sys.argv) != 3:
        print("Использование: python gcd.py <число1> <число2>")
        return

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = gcd(num1, num2)
        print(f"Наибольший общий делитель чисел {num1} и {num2}: {result}")
    except ValueError:
        print("Введите два целых числа.")


if __name__ == "__main__":
    main()
