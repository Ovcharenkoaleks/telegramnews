import requests
from bs4 import BeautifulSoup


def get_sports_news():
    url = 'https://www.championat.ru/news/1.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edge/90.0.818.66'
    }

    response = requests.get(url, headers=headers)
    print(f"Статус код ответа: {response.status_code}")

    if response.status_code != 200:
        print("Ошибка при запросе страницы")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    news = []
    # Мы ищем теги <a> с классом 'news-item__title'
    for item in soup.find_all('a', class_='news-item__title'):
        title = item.text.strip()  # Извлекаем текст заголовка
        link = 'https://www.championat.ru' + item['href']  # Полный URL для ссылки на новость
        news.append({'title': title, 'link': link})

    print(f"Найдено новостей: {len(news)}")
    return news


# Пример использования функции
news = get_sports_news()
for article in news:
    print(f"{article['title']} - {article['link']}")

