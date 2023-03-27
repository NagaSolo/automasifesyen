import pandas as pd


def articles_reader(filename='data_input/Question_1_Dataset.xlsx'):
    sanitized_articles = []
    df = pd.read_excel(filename)
    articles = df['Article Number'].dropna().astype(int).astype(str).tolist()
    for article in articles:
        if len(article) < 10:
            sanitized_articles.append('0' + article)
        else:
            sanitized_articles.append(article)
    return sanitized_articles

# print(articles_reader())