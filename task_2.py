import pandas as pd

# Загрузка данных
df = pd.read_csv('credit.csv') # просим прочитать файл и закидываем его в переменную

# Task_2 Фильтрация данных

# Все пассажиры старше 30

filtered_df_Age = df[df['age'] > 30] # применяется метод логического индексирования

print(filtered_df_Age)

# Пассажиры 1-го класса пох)
filtered_df_real_estate = df[df['real_estate'] == 1]

print(filtered_df_real_estate)