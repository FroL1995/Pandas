import pandas as pd

# Загрузка данных
df = pd.read_csv('credit.csv') # просим прочитать файл и закидываем его в переменную

# Task_4 Агрегация

# Среднее, медиана и максимум для возраста
print(df['Age'].agg(['mean', 'median', 'max']))

# Средний возраст по полу
print(df.groupby('late_60_89')['Age'].mean())
