import streamlit as st
from news_api import get_news, filter_removed_articles
from text_processing import preprocess_text, analyze_sentiment, generate_summary

def app():
    st.title('Оптимизированное приложение: Резюмирование новостей с тональностью')

    api_key = ""
    query = st.text_input('Введите тему для поиска новостей (например, "технологии"):')
    max_articles = st.slider('Максимальное количество статей:', 1, 10, 5)

    if query:
        st.write(f"Ищем новости по теме: {query}")
        news_articles = get_news(api_key, query, max_articles)
        news_articles = filter_removed_articles(news_articles)

        if news_articles:
            articles_with_sentiment = []
            for article in news_articles:
                processed_description = preprocess_text(article['description'])
                articles_with_sentiment.append({
                    'title': article['title'],
                    'description': processed_description,
                    'summary': generate_summary(processed_description),
                    'sentiment': analyze_sentiment(processed_description),
                    'published_at': article['publishedAt'],
                    'url': article['url']
                })

            sentiment_filter = st.radio("Выберите фильтр по тональности:", ("Все", "Позитивный", "Негативный", "Нейтральный"))
            filtered_articles = [article for article in articles_with_sentiment if sentiment_filter == "Все" or article['sentiment'] == sentiment_filter]

            for article in filtered_articles:
                st.subheader(article['title'])
                st.write(f"Описание: {article['description']}")
                st.write(f"Резюме: {article['summary']}")
                st.write(f"Тональность: {article['sentiment']}")
                st.write(f"Дата публикации: {article['published_at']}")
                st.write(f"Ссылка: [Читать статью]({article['url']})")
        else:
            st.write("Нет новостей по запросу.")

if __name__ == "__main__":
    import torch
    torch.set_num_threads(1)
    app()
