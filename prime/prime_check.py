def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True  # 2 и 3 — простые числа
    if num % 2 == 0 or num % 3 == 0:
        return False  # Четные числа и кратные 3 — составные

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


# Пример использования
number = 1715232653
if is_prime(number):
    print(f"{number} – простое число")
else:
    print(f"{number} – составное число")
