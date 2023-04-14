import matplotlib.pyplot as plt
import pandas as pd

# Создание объекта Figure и двух подграфиков
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 8))

# Загрузка данных для первого графика
data1 = pd.read_csv('btcusdt_data_6m_2.csv')

# Построение первого графика
ax[0].plot(data1['timestamp'], data1['price'], color='blue')
ax[0].set_title('BTC')

# Загрузка данных для второго графика
data2 = pd.read_csv('ETHUSDT_data_6m_2.csv')

# Построение второго графика
ax[1].plot(data2['timestamp'], data2['price'], color='green')
ax[1].set_title('ETH')

# Отображение графиков
plt.show()
