import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['sanidhya', 'shivam', 'yash', 'Dev'],
    'score': [2 , 12 , 45 , 75]})

df2 = pd.DataFrame({
    'id': [3, 4, 5, 6],
    'score': [85 , 90 , 75 , 60]})
print( pd.merge(df1, df2, on='id', how='inner'))

print(pd.merge(df1, df2, on='id', how='left'))

print(pd.merge(df1, df2, on='id', how='right'))
print(pd.merge(df1, df2, on=['id', 'score'], how='inner'))