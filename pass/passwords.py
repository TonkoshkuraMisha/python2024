import secrets
import string


def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
    # Определяем символьные наборы для пароля
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if special_chars:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one type of character must be selected.")

    # Генерируем пароль из символов заданной длины
    password = ''.join(secrets.choice(chars) for _ in range(length))

    # Проверка на присутствие каждого типа символов
    if uppercase and not any(c.isupper() for c in password):
        password = password[:length - 1] + secrets.choice(string.ascii_uppercase)
    if lowercase and not any(c.islower() for c in password):
        password = password[:length - 1] + secrets.choice(string.ascii_lowercase)
    if digits and not any(c.isdigit() for c in password):
        password = password[:length - 1] + secrets.choice(string.digits)
    if special_chars and not any(c in string.punctuation for c in password):
        password = password[:length - 1] + secrets.choice(string.punctuation)

    # Перемешиваем символы, чтобы гарантировать случайность
    password = ''.join(secrets.choice(password) for _ in range(length))

    return password


# Пример использования
length = 12
password = generate_password(length)
print("Сгенерированный пароль:", password)
