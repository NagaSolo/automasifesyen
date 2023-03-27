import pandas as pd

def output_list():
    sanitized_datas = []
    df_output = pd.read_csv('available_articles.csv')
    articles_output = df_output['article_id'].dropna().astype(str).tolist()
    for article in articles_output:
        if len(article) < 10:
            sanitized_datas.append('0' + article)
        else:
            sanitized_datas.append(article)
    return sanitized_datas


def input_list():
    sanitized_datas = []
    df = pd.read_excel('data_input/Question_1_Dataset.xlsx')
    
    articles = df['Article Number'].dropna().astype(int).astype(str).tolist()
    names = df['Product Name'].dropna().tolist()
    colors = df['Color'].dropna().tolist()
    for count, article in enumerate(articles):
        if len(article) < 10:
            sanitized_datas.append(('0' + article, names[count], colors[count]))
        else:
            sanitized_datas.append((article, names[count], colors[count]))
    return sanitized_datas


def compare_input_output():
    inputs, outputs = input_list(), output_list()
    for i in inputs:
        if i[0] not in outputs:
            print(i[0], i[1], i[2], sep=' | ')
        else:
            continue


if __name__ == '__main__':
    compare_input_output()