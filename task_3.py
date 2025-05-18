import pandas as pd

# Загрузка данных
df = pd.read_csv('credit.csv') # просим прочитать файл и закидываем его в переменную

# Task_3 Сортировка

# Сортировка по убыванию цены билета
df_sorted = df.sort_values('debt_ratio', ascending=False)
print(df_sorted.head())

# Топ-5 самых дорогих билетов
print(df.nlargest(10, 'debt_ratio'))