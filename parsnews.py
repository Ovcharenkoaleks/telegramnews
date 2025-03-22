import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL страницы с новостями футбола
url = "https://www.championat.ru/football/"

# Заголовок user-agent, чтобы не заблокировали запросы
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Получаем текущую дату в формате YYYY-MM-DD
current_date = datetime.now().strftime("%Y-%m-%d")

# Формируем имя файла с текущей датой
filename = f"news_titles_and_links_{current_date}.txt"

# Получаем страницу с новостями футбола
response = requests.get(url, headers=headers)
print(f"Подключение к странице {url}... Статус код: {response.status_code}")  # Логируем статус подключения

# Проверяем успешность запроса
if response.status_code == 200:
    # Парсим страницу
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем все теги <a> с классом 'news-item__title', что соответствует заголовкам новостей
    news_links = soup.find_all('a', class_='news-item__title', href=True)

    print(f"Найдено {len(news_links)} новостных заголовков.")  # Логируем количество найденных заголовков

    # Открываем файл для записи
    with open(filename, "w", encoding="utf-8") as file:
        # Проходим по каждому заголовку и ссылке
        for link in news_links:
            title = link.get_text(strip=True)
            href = link.get('href')

            # Формируем полный URL
            full_link = f"https://www.championat.ru{href}" if href.startswith('/') else href

            # Записываем заголовок и ссылку новости в файл
            file.write(f"Заголовок: {title}\n")
            file.write(f"Ссылка: {full_link}\n\n")

    print(f"Заголовки и ссылки новостей успешно записаны в файл {filename}.")
else:
    print(f"Ошибка при подключении к {url}, статус код: {response.status_code}")
