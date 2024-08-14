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


def prime_factors(num):
    factors = []
    # Делим число на 2, пока оно делится
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    # Делим число на 3, пока оно делится
    while num % 3 == 0:
        factors.append(3)
        num //= 3
    # Проверяем числа вида 6k ± 1
    i = 5
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num //= i
        while num % (i + 2) == 0:
            factors.append(i + 2)
            num //= (i + 2)
        i += 6
    # Если num всё еще больше 2, значит это простое число
    if num > 2:
        factors.append(num)
    return factors


# Пример использования
number = 1715232653
if is_prime(number):
    print(f"{number} – простое число")
else:
    factors = prime_factors(number)
    print(f"{number} – составное число. Простые множители: {factors}")
