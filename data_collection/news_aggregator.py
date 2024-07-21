import requests
import json

def get_news(api_key, query='stock market'):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    news_data = response.json()
    return news_data['articles']

if __name__ == "__main__":
    api_key = 'your_newsapi_key'
    articles = get_news(api_key)
    with open('news_articles.json', 'w') as f:
        json.dump(articles, f)
