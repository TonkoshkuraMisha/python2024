def is_palindrome(string):
    left, right = 0, len(string) - 1

    while left < right:
        # Пропускаем пробелы и приводим к нижнему регистру
        while left < right and not string[left].isalnum():
            left += 1
        while left < right and not string[right].isalnum():
            right -= 1

        if string[left].lower() != string[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Пример использования
word = "А роза упала на лапу Азора"
if is_palindrome(word):
    print(f"Строка '{word}' является палиндромом.")
else:
    print(f"Строка '{word}' не является палиндромом.")
