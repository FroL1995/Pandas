import pandas as pd


# Task_1 Загрузка данных

# Загрузка данных
df = pd.read_csv('credit.csv') # просим прочитать файл и закидываем его в переменную

# Первые 5 строк
print(df.head()) # голова объекта (первые пять строк): просим их выдать



# Получение количества строк
num_rows = df.shape[0]

# Получение количества столбцов
num_cols = df.shape[1]

print(f"Количество строк: {num_rows}")
print(f"Количество столбцов: {num_cols}")

# shape возвращает кортеж (число строк, число столбцов). Например, df.shape вернет (100, 5), если DataFrame df содержит 100 строк и 5 столбцов.



# Task_2 Фильтрация данных

# Все пассажиры старше 30

filtered_df_Age = df[df['age'] > 30] # применяется метод логического индексирования

print(filtered_df_Age)

# Пассажиры 1-го класса пох)
filtered_df_real_estate = df[df['real_estate'] == 1]

print(filtered_df_real_estate)



# Task_3 Сортировка

# Сортировка по убыванию цены билета
df_sorted = df.sort_values('debt_ratio', ascending=False)
df_sorted.head()

# Топ-5 самых дорогих билетов
df.nlargest(5, 'debt_ratio')
