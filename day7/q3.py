import pandas as pd 
import numpy as np

df = pd.read_csv('data.csv')
print(df)
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())
print(df.tail())
print(df.to_string())
grouped = df.groupby(['Gender', 'Age']).sum()
print(grouped)
