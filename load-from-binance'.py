import requests
import pandas as pd

# Установите начальную и конечную даты для получения исторических данных
# Установите начальную и конечную даты для получения исторических данных
interval = '1m'
symbol = 'BTCUSDT'
start_time = 100000000000 # 1 января 2018 года в миллисекундах
end_time = start_time + (365 * 24 * 60 * 60 * 1000) # 1 год в миллисекундах
url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_time}&endTime={end_time}'

# Загрузите данные
response = requests.get(url)
data = response.json()

# Преобразуйте данные в формат DataFrame и сохраните их в CSV-файл
df = pd.DataFrame(data, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
                                 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
                                 'Taker buy quote asset volume', 'Ignore'])
df.to_csv('btcusdt_data.csv', index=False)

# Выведите первые несколько строк данных
print(df.head())
