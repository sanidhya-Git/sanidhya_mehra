import pandas as pd 
data= [[1, 'skit', 85],
              [2, 'new', 90],
              [3, 'area', 95]]

df = pd.DataFrame(data, columns=['ID', 'Name', 'Score'])
print(df)
