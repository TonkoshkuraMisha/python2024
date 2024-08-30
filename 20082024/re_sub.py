import re

# Читаем входную строку
input_str = input()

# Заменяем все подряд идущие дефисы на один дефис
output_str = re.sub(r'-{2,}', '-', input_str)

# Выводим результат
print(output_str)
