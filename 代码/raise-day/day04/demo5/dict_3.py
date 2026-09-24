"""
    字典的遍历
    keys() 函数获取所有的键 然后再根据键获取值
    values() 函数获取所有的值
    items() 获取所有的键值对
"""
from day04.demo1.test_list_3 import value

print("---------------------字典的遍历 keys函数----------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

keys = dict1.keys()

print(keys)
print(type(keys))

# 遍历键的容器
for key in keys:
    # 根据键获取值
    print(key,dict1[key],dict1.get(key))

print("---------------------字典的遍历 values函数----------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

values = dict1.values()

print(values)
print(type(values))

for value in values:
    print(value)

print("---------------------字典的遍历 items函数----------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

items = dict1.items()
for key, value in items:
    print(key,value)