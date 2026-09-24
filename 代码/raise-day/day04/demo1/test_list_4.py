"""
    列表操作
"""

print("----------------列表的删除操作----------------")

list1 = [11, 22, 33, 44, 55]

del list1[0] # 直接删除指定的下标元素

print(list1)

print("----------------嵌套列表的操作----------------")

list12 = [[1, 2, 3],['a','b','c'],[True,False,True]]

for item in list12:
    # print(item) # 直接输出 属于打印外层列表中的每一个小(子)列表
    for value in item: # 嵌套循环 继续迭代内层的列表
        print(value,end="\t")
    print()

print("----------------列表推导式----------------")

# 通过表达式的方式 快速创建一个列表

list1 = [i for i in range(1,11)] # i的取值从1~10 存放在列表中

print(list1)

list2 = [x**2 for x in range(5)] # i的取值从1~10 再**2 存放在列表中

print(list2)

list3 = [x**2 for x in range(5) if x % 2 ==0] # i的取值从0~4 只筛选偶数 再**2 存放在列表中

print(list3)

list1 = [11, 22, 33, 44, 55]

list2 = list1[:]

print(list2)

list3 = [x for x in list1] # 通过列表推导式的方式复制一个列表

print(list3)

list4 = ['a','b','c']

list5 = [1,2,3]

list6 = [(i,j) for i in list4 for j in list5]

print(list6)

print("----------------列表Zip函数----------------")

# 将两个列表打包在一起

list4 = ['a','b','c']

list5 = [1, 2, 3, 4]

zipped = zip(list4,list5) # 如果两个列表长度不一致 以长度短的为主

print(zipped)

list6 = list(zipped)

print(list6)

print("----------------列表list函数 转换列表----------------")

list_1 = list("abcdef")

print(list_1)

list_1 = list("123456")

print(list_1)

list_1 = list((1,2,3,4,5)) # 传入元组类型

print(list_1)