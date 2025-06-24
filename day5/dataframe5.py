import pandas as pd 
data = [
    {'ID': 1, 'Name': 'sanidhya', 'Score': 85},
    {'ID': 2, 'Name': 'shivam ','Score': 90},
    {'ID': 3, 'Name': 'luck', 'Score': 95}
]

df = pd.DataFrame(data)
print(df)