import pandas as pd 

data = {
    'ID': [1, 2, 3],
    'Name': ['sanidhya', 'deval', 'shivam'],
    'Score': [85, 90, 95]
}

df = pd.DataFrame(data)

print(df)