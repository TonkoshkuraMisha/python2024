import requests

# Начальная ссылка на первый файл
url = 'https://stepik.org/media/attachments/course67/3.6.3/699991.txt'

while True:
    # Скачиваем текущий файл
    response = requests.get(url)
    response.raise_for_status()  # Проверка на успешный ответ

    # Получаем текст файла
    text = response.text.strip()

    # Проверяем, начинается ли текст с "We"
    if text.startswith('We'):
        # Если да, выводим содержимое и завершаем цикл
        print(text)
        break

    # Иначе, извлекаем ссылку на следующий файл
    url = 'https://stepik.org/media/attachments/course67/3.6.3/' + text
