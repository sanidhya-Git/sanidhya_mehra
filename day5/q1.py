import pandas as pd
data = {'a': 10, 'b': 20, 'c': 30}
s = pd.Series(data)
print(s)

print("\n--------------from tuple------")
data2 = (100, 200, 300)
s2 = pd.Series(data2)
print(s2)

print("\n--------------printing elements-----")

print(s['b']) 
print(s2[1])  
print(s2[0:])
