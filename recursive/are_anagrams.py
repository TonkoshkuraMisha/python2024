from collections import Counter
import string


def are_anagrams(str1, str2):
    # Удаляем пробелы и знаки препинания, приводим строки к нижнему регистру
    str1_cleaned = ''.join(char.lower() for char in str1 if char.isalnum())
    str2_cleaned = ''.join(char.lower() for char in str2 if char.isalnum())

    # Сравниваем частоты символов
    return Counter(str1_cleaned) == Counter(str2_cleaned)


# Пример использования
string1 = ''.join(sorted(string.ascii_lowercase))  # 'abcdefghijklmnopqrstuvwxyz'
string2 = "The quick brown fox jumps over the lazy dog"

if are_anagrams(string1, string2):
    print(f"'{string1}' и '{string2}' – анаграммы.")
else:
    print(f"'{string1}' и '{string2}' – не анаграммы.")
