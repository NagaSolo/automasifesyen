import pandas as pd

filename = 'Question_1_Dataset.xlsx'
df = pd.read_excel(filename)
print(df['Article Number'].dropna().astype(int).astype(str))