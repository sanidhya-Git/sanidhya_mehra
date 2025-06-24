import pandas as pd 
data =[[1 , 'sanidhya' , 12] , 
       [2 , 'deval' , 13],
       [3 , 'yash' , 14]]
df = pd.DataFrame(data , columns = ['id' , 'name' , 'age'])
print(df)