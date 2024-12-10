import requests
import streamlit as st

def get_news(api_key, query='', max_articles=5):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code != 200:
        st.error(f"Ошибка: {response.status_code}")
        return []
    news_data = response.json()
    articles = news_data.get('articles', [])
    return articles[:max_articles]

def filter_removed_articles(articles):
    return [article for article in articles if "removed" not in article.get('title', '').lower() and "removed" not in article.get('description', '').lower()]
