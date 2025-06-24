import pandas as pd 
data = [(1, 'sanidhya', 85),
               (2, 'coplur', 90),
               (3, 'shivam', 95)]

df= pd.DataFrame(data, columns=['ID', 'Name', 'Score'])

print(df)