import requests
import pandas as pd

# Установите начальную и конечную даты для получения исторических данных
interval = '1d'  # интервал дней
symbol = 'ETHUSDT'
end_time = pd.Timestamp.now()  # текущее время
start_time = end_time - pd.Timedelta(days=180)  # 180 дней назад
start_time = int(start_time.timestamp() * 1000)  # перевод в миллисекунды
end_time = int(end_time.timestamp() * 1000)  # перевод в миллисекунды

# Загрузите данные
url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_time}&endTime={end_time}'
response = requests.get(url)
data = response.json()

# Преобразуйте данные в формат DataFrame и сохраните их в CSV-файл
df = pd.DataFrame(data, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
                                 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
                                 'Taker buy quote asset volume', 'Ignore'])

df = df[['Close time', 'Close']]
df.columns = ['timestamp', 'price']
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

df.to_csv('{}_data_6m_2.csv'.format(symbol), index=False)

# Выведите первые несколько строк данных
print(df.head())
