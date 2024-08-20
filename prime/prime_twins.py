def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 и 1 не являются простыми числами

    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]


def find_prime_twins_in_range(start, end):
    primes = []

    # Используем Решето Эратосфена до верхней границы
    all_primes_up_to_end = sieve_of_eratosthenes(end)

    # Отбираем простые числа, которые попадают в нужный диапазон
    primes_in_range = [p for p in all_primes_up_to_end if p >= start]

    # Ищем простые числа-близнецы
    twin_primes = [(primes_in_range[i], primes_in_range[i + 1])
                   for i in range(len(primes_in_range) - 1)
                   if primes_in_range[i + 1] - primes_in_range[i] == 2]

    return twin_primes


# Пример использования
start_range = 1
end_range = 100000
twin_prime_numbers = find_prime_twins_in_range(start_range, end_range)
print(f"Прості числа-близнюки у діапазоні від {start_range} до {end_range}:")
print(*twin_prime_numbers)
