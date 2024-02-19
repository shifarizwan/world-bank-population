# -*- coding: utf-8 -*-
"""Copy of Untitled39.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RungeoUt5hA53KS33qdyN30W_fhMGdzW
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter, YearLocator

print(df.columns)
print(df.info())

if '1990' not in df.columns:
    print("'1990' column not found in DataFrame.")

country_by_1990_values = df.sort_values(by='1990').head(11)

country_by_1990_t = country_by_1990_values.set_index('Country Name').T

df = pd.read_csv("/content/P_Data_Extract_From_World_Development_Indicators.csv")
print (df)

df = pd.read_csv("/content/P_Data_Extract_From_World_Development_Indicators.csv")
print (df)

df.head()

df.tail()

df.shape

df.columns

df.dtypes

df.info()

df.describe()

df.duplicated().sum()

df.isna().sum().any()

df = df.fillna(method = "ffill")
df.head()

df.isna().sum().any()

df['Country Name'].unique()

df['Country Name'].unique()

print(df.head())

df['Series Name'].unique()

df['Series Code'].unique()

print(df.columns)

df['Series Name'] = 'Your Series Name'
df['Series Code'] = 'Your Series Code'
df['Country Code'] = 'Your Country Code'

df.columns

cols =['1990', '2000', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020',
       '2021', '2022']

print(df.columns)

print(df.columns)

for col in ['Series Name','Series Code','Country Code']:
    if col not in df.columns:
        print(f"{col} not found in DataFrame columns.")

cols = ['Country Name']
for i in cols:
    fig = plt.figure(figsize=(5,3))
    plt.hist(df[i], color='#B22222', bins=10)
    plt.xlabel(i)
    plt.show()

years = df.columns[1:]
total_values = df [years].sum()
plt.figure(figsize=(100, 50))
plt.barh(years, total_values,color='#191970')
plt.xlabel('Total Values')
plt.ylabel('Year', size=100)
plt.title('Total Values per Year', size=50)
plt.show()

print(df.columns)

print(df.info())

if '1990' not in df.columns:
    print("'1990' column not found in DataFrame.")

country_by_1990_values = df.sort_values(by='1990').head(11)
print(country_by_1990_values)

for country_name, data_values in country_by_1990_t.iterrows():
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(x=data_values.index, y=data_values.values)
    plt.xlabel('Years')
    plt.ylabel('Data Values')
    plt.title(f"{country_name} - Data Values from 1990 to 2022")
    plt.xticks(rotation=90)
    # Remove missing years from the x-axis
    plt.xlim(xmin=1990, xmax=2022)
    plt.gca().xaxis.set_major_formatter(DateFormatter('%Y'))
    plt.gca().xaxis.set_major_locator(YearLocator())
    plt.show()

