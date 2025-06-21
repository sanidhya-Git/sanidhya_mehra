# # # d = {1:"sanidhya" , 2 :"yash " , 3:{1:"one" , 2 :"two"}}
# # # print(d[1])
# # # print(d[3])
# # # print(d[3][1])
# #
# # dict={}
# # print(dict)
# # dict[0]="python"
# # dict[1]="py"
# # dict[2]="pyth"
# # # dict.popitem()
# # print(dict.popitem())
# # print(dict)
# # # dict.pop(1)
# # # print(dict)
# # # print(dict.get(2))
# # # print(dict.items())
# # # del(dict[1])
# # # # pop(1)
# # # print(dict)
# # # dict2 = dict.copy()
# # # print(dict2)
# # # dict.clear()
# # # #
# # dic ={"a":1 , "b":2}
# # di ={"c":3 , "d":4}
# #
# # di.update(dic)
# # print(di)
#t
# l =[]
# while True:
#     print("")
from itertools import count

# t = (1 , 2 , 3 ,4 ,5)
# for x in range (1):
#     print( ,t[0:])
# print(t)
# print(type(t))
# t = ('fdffdf',)*3
# print(t)
# l = (1 , 2)
# print(len(l))

# l = [10 , 20 , 30]
# t = tuple(l)
# print(t)
# print(sum(t))
# print(min(t))
# print(max(t))
# print(count(10))

# s ={"a" , "b" , "c"}
# print(s)

# s = {"apple" , "banana", "cherry"}
# S2 = {"abc", 10 ,20 }
# s3 = s.uniform(s2)

# s5=set()
# s6=set()
# for i in range(5):
#     s5.add(i)
# for i in range(3,9):
#     s6.add(i)
# s7=s5.intersection(s6)
# print(s7)
# s8 = s5&s6
# print(s8)
# def sanidhya(a=0 ,b=0):
#     res = a + b
#     return res
# sanidhya(10 ,12)
# print(sum)
# def palce(city3 , city2 , city1):
#     print("the first city " +city1)
# palce("a" ,"b" , "c")
#
#
# def places(*city):
#     print(city[0])
# places("a" , "b", "c")

# f = open("new1.txt" ,"r")
# for each in f:
#     print(each)
# f.write("this is the python program ")
# f.close()
# f = open("new1.txt" ,"r")
# print(f.read())

with open("new1.txt" ) as file:
    data = file.readlines()
    for line in data:
        word=line.split()
        print(word)



# print(data)