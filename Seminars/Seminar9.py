# РАБОТА С ТАБЛИЧНЫМИ ДАННЫМИ
# Задача №57
'''
1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
'''
'''
from pandas import read_csv
data = read_csv('california_housing_test.csv')
print(type(data))
print(data.shape)  # Кол строк и столбцов
print(data.dtypes)  # Типы данных
print(data.info())  # Более подробная инфа о столбцах (метаданные)
print(data.describe())  # Общая статистика:
'''
# Задача №59.
'''
1. Проверить есть ли в файле пустые значения 
2. Показать median_house_value где median_income < 2 
3. Показать данные в первых 2 столбцах 
4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
'''
# from pandas import read_csv
# data = read_csv('california_housing_test.csv')
# print(data.isnull())  # Выводит True для пустых значений
# print(data.isnull().sum()) # Выводит количество пустых значений по столбцам
# print(data[data['median_income'] < 2]['median_house_value'])
# print(data.columns)

# print(data.iloc[:, :2])  # Все строки и первые 2 столбца
# print(data[(data['housing_median_age'] < 20) & (data['median_house_value'] > 70000)][['longitude', 'latitude']])

# Задача №61.
'''
1. Определить какое максимальное и минимальное значение median_house_value 
2. Показать максимальное median_house_value, где median_income = 3.1250 
3. Узнать какая максимальная population в зоне минимального значения median_house_value
'''
# from pandas import read_csv
# data = read_csv('california_housing_test.csv')

# print(f'Минимальное значение: {data['median_house_value'].min()}, максимальное значение: {data['median_house_value'].max()}')

# print(data[data['median_income'] == 3.1250]['median_house_value'].max())

# print(data[data['median_house_value'] == data['median_house_value'].min()]['population'].max())
# print(data.columns)

# ДОМАШКА
# Задача 1
'''

Дан файл california_housing_train.csv. 
Определить среднюю стоимость дома , 
где количество людей от 0 до 500 (population) 
и сохранить ее в переменную avg.
Используйте модуль pandas.
'''
'''
from pandas import read_csv
data = read_csv('california_housing_test.csv')
avg = data[data['population'] < 500]['median_house_value'].mean()
'''

# Задача 2
'''
Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" 
в зоне минимального значения переменной min_population 
и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas
'''
from pandas import read_csv
data = read_csv('california_housing_test.csv')
max_households_in_min_population = data[data['population'] == data['population'].min()]['households'].max()
print(max_households_in_min_population)