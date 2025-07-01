# # from operator import inv

# # import numpy as np 
# # # arr = np.array([[1 , 2 , 3 ] , [2 , 4 , 5] , [6 , 7, 4] ,[1 , 7 , 8]])
# # # print(arr[0])
# # # print(arr)    
# # # arr[:,[2,1]]=arr[:,[1 ,2]]
# # # print('\n',arr)
# # # arr[[2,1],:]=arr[[1 ,2],:]
# # # print('\n',arr)
# # # arr[[2,1],[1]]=arr[[1 ,2],[1]]
# # # print('\n',arr)
# # # arr[[1],[2,1]]=arr[[1],[1 ,2]]
# # # print('\n',arr)
# # # arr[:,[0,1,2]]=arr[:,[1,2,0]]
# # # print('\n',arr)



# # # arr = np.array([[[1 , 2 , 3 ] , [2 , 4 , 5]], [[6 , 7, 4] ,[1 , 7 , 8]]])
# # # arr[:,[1],[0,2]]= arr[:,[1],[2,0]]
# # # print('\n',arr)
# # # arr[[0,1] , [1] , :]= arr[[1,0],[1],:]
# # # print('\n',arr)
# # # arr[:,[0,1],:]= arr[:,[1,0],:]
# # # print('\n',arr)


# # # arr =np.array([1 , 2 , np.nan, np.nan , 4])
# # # emp= np.isnan(arr)
# # # rep = np.nan_to_num(arr , copy=True, nan=4)
# # # print(emp)
# # # print(rep)
# # # a=np.nan_to_num(arr , copy=False , nan=0, posinf=True, neginf=False)
# # # print(a)


# # # arr = np.array([[[1 , 2 , 3 ] , [2 , 4 , 5]], [[6 , 7, 4] ,[1 , 7 , 8]]])
# # # arr1 = np.array([[[1 , 2 , 3 ] , [2 , 4 , 5]], [[6 , 7, 4] ,[1 , 7 , 8]]])
# # # np.save('data.npy', arr , arr1)
# # # np.savez('data.npz', arr , arr1)

# # # res=np.load('data.py')
# # # print(res['arr'])
# # # print(res['arr1'])
# # # with open ('data.txt', 'w') as f:
# # #     f.write("1.0 2.0 3.0 \n4.0 5.0 6.0 \n7.0 8.0 9.0")

# # # res = np.loadtxt('data.txt')
# # # data = np.array([[1, 2, 3], [4, 5, 6]])
# # # res=np.savetxt('data.txt', data, fmt='%1.1f' , delimiter=' ')      
# # # file=np.loadtxt('data.txt')   
# # # gen=np.genfromtxt('data.txt', delimiter=',')                  
# # # # print(res )
# # # print(file)
# # # print(gen)

# # arr = np.array([[2,8], [9,5]])
# # arr1 =np.array([2 ,2 ])

# # a = np.linalg.solve(arr, arr1 )
# # print(a)
# # inv=np.linalg.inv(arr)

# # print(inv)






 
# from calendar import c
# from turtle import color
# from matplotlib.lines import lineStyles
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# # x = np.linspace(0 ,10 , 100)
# # y =np.sin(x)
# # plt.plot(x,y,label='sin(x)' , color='red' , linestyle='--' )

# # plt.xlabel('x')
# # plt.ylabel('y')
# # plt.title('sin(x)')
# # plt.legend()
# # plt.grid(True)
# # plt.scatter(x, y, color='blue', marker='o', s=10, label='data points')



# # plt.fill_between(x, y, color='lightblue', alpha=0.5, label='area under curve')
# # plt.annotate('Local Max', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.5),
# #              arrowprops=dict(facecolor='black', shrink=0.05),   )
# # plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
# # plt.axvline(np.pi, color='black', linewidth=0.5, linestyle='--')
# # plt.xticks(np.arange(0, 11, 1))





# categories=['A','B','C','D']
# size=[10,20,40,40]
# # plt.bar(categories,value,color='yellow',edgecolor='black',width=0.4)
# plt.pie(size,labels=categories,autopct='%1.1f%%',startangle=140,colors=['red','blue','green','yellow'],explode=(0.1,0,0,0),shadow=True)
# plt.title('Pie Chart Example')
# plt.axis('equal')  
# plt.show()