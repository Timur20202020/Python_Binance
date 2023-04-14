import pandas as pd

# Загрузите CSV-файл с данными
df = pd.read_csv('btcusdt_data.csv')

# Удалите ненужные столбцы
df.drop(['Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
         'Taker buy quote asset volume', 'Ignore'], axis=1, inplace=True)

# Преобразуйте столбец 'Open time' из формата миллисекунд в формат даты и времени
df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')

# Установите 'Open time' в качестве индекса DataFrame
df.set_index('Open time', inplace=True)

# Масштабируйте столбцы 'Open', 'High', 'Low', 'Close' и 'Volume' на основе столбца 'Close'
df[['Open', 'High', 'Low', 'Close', 'Volume']] = df[['Open', 'High', 'Low', 'Close', 'Volume']].div(df['Close'], axis=0)

# Удалите строки с пропущенными значениями
df.dropna(inplace=True)

# Сохраните обработанные данные в CSV-файл
df.to_csv('btcusdt_data_processed.csv', index=True)

# Выведите первые несколько строк обработанных данных
print(df.head())
