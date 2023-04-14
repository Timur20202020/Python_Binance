import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style


# Загружаем данные из csv файла
# sep - формат данных на основе регулярных выражений, чтобы не быдо ошибок
data = pd.read_csv('./btcusdt_data_6m_2.csv',sep=r'\s*,\s*', header=0, encoding='utf8', engine='python')

# стиль графика
style.use('ggplot')

# преобразуем значения из csv в понятный для библиотеки формат
x = data['timestamp'].to_numpy()
y = data['price'].to_numpy()


# даем название осям и графику
plt.xlabel('Дата')
plt.ylabel('Цена')
plt.title('Анализ цены за 2022-2023 год')


# рисуем точки
plt.plot(x, y)

# показываем график
plt.show()