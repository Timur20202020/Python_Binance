import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Загрузить данные из файла csv
df = pd.read_csv('btcusdt_data.csv')

# Удалить столбец "Ignore"
df = df.drop(['Close'], axis=1)

# Преобразовать столбец "Open time" в формат даты и времени
df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')

# Преобразовать столбец "Open time" в числовой формат Unix timestamp
df['Open time'] = df['Open time'].apply(lambda x: x.timestamp())

# Разделить данные на обучающую и тестовую выборки
train_data, test_data = train_test_split(df.values, test_size=0.2, random_state=42)

train_data = train_data.astype(np.float64)
test_data = test_data.astype(np.float64)

# Сохранить данные в файлы CSV
np.savetxt('train_data.csv', train_data, delimiter=',')
np.savetxt('test_data.csv', test_data, delimiter=',')

# Вывести размеры обучающей и тестовой выборок
print(f"Размер обучающей выборки: {train_data.shape}")
print(f"Размер тестовой выборки: {test_data.shape}")
