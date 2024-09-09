from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Настройки прокси
PROXY = "127.0.0.1:8080"

chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={PROXY}')
chrome_options.add_argument('--ignore-certificate-errors')  # Игнорируем ошибки сертификатов

# Убедитесь, что путь к chromedriver правильный
service = Service(executable_path='path/to/chromedriver')

# Инициализация драйвера с установленным прокси
driver = webdriver.Chrome(service=service, options=chrome_options)

# Открываем игру
game_url = "https://www.playngo.com/games/fire-joker"
driver.get(game_url)

# Ваш дальнейший код
