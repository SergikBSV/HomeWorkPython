"""
Самостоятельная практика №1
Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
Посмотреть сколько в нем строк и столбцов
(Доп) Определить какой тип данных имеют столбцы
(Доп) Проверить есть ли в файле пустые значения

Самостоятельная практика №2
Показать median_house_value где median_income < 2
(Доп) Показать данные в первых 2 столбцах
(Доп) Выбрать данные где housing_median_age < 20 и median_house_value > 70000

Самостоятельная практика №3
Определить какое максимальное и минимальное значение median_house_value
(Доп) Показать максимальное median_house_value, где median_income = 3.1250
(Доп) Узнать какая максимальная population в зоне минимального значения median_house_value
"""

import pandas as pd

df = pd.read_csv('california_housing_test.csv')

print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

print(df.loc[df['median_income'] < 2, ['median_house_value']])
print(df.iloc[:, :2])
print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])

print(df['median_house_value'].max())
print(df['median_house_value'].min())
print(df[df['median_income'] == 3.1250]["median_house_value"].max())
print(df[df["median_house_value"] == df["median_house_value"].min()]["population"].max())


