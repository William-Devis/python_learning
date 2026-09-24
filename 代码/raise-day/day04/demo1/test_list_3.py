"""
    列表的遍历操作
"""
print("-----------------------列表的遍历操作----------------------")

list1 = [11, 22, 33, 44, 55]

for i in list1:
    print(i)

print("-----------------------列表的遍历操作----------------------")

for i in range(len(list1)):
    print(i,list1[i])

print("-----------------------列表的遍历操作 使用enumerate函数 ----------------------")

for i , value in enumerate(list1):
    print(i,value)

print("-----------------------列表的遍历操作 使用enumerate函数 指定start参数----------------------")

for i , value in enumerate(list1,start=1): # 可以指定起始的标记数值 依然是从0下标开始遍历 只是数值改变了
    print(i,value)
