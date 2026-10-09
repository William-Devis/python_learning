"""
    关于直接赋值 深拷贝 浅拷贝
"""

print("---------------------直接赋值 属于复制的地址值--------------------")

list1 = [1,2,3,4,5,6]

list2 = list1

print(list1)
print(list2)
print(id(list1),id(list2))

print("---------------------浅拷贝 创建新的外层对象 内层对象继续复用--------------------")

list1 = [1,2,3,[4,5,6]]

list2 = list1.copy()

print(list1,list2)
print(id(list1),id(list2))

print(list1[0] is list2[0])
print(id(list1[0]),id(list2[0]))

print(list1[1] is list2[1])
print(id(list1[1]),id(list2[1]))

print(list1[2] is list2[2])
print(id(list1[2]),id(list2[2]))

print(list1[3] is list2[3])
print(id(list1[3]),id(list2[3]))

print("---------------------深拷贝 从外到内 全部是新的--------------------")

import copy

list1 = [1,2,3,[4,5,6]]

list2 = copy.deepcopy(list1)

print(list1,list2)
print(id(list1),id(list2))

print(list1[0] is list2[0])
print(id(list1[0]),id(list2[0]))

print(list1[1] is list2[1])
print(id(list1[1]),id(list2[1]))

print(list1[2] is list2[2])
print(id(list1[2]),id(list2[2]))

print(list1[3] is list2[3])
print(id(list1[3]),id(list2[3]))




