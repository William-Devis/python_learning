"""
    一个无序的键值对集合，键是唯一的，而值可以重复。
    字典使用 {} 定义，键 (key) 和值 (value) 使用 ：连接，每个键值对之间使用，分隔。如{key1 : value1, key2 : value2}
    字典没有索引。
    字典可以通过键来获取对应的值。
    值可以取任何数据包类型，但键必须是不变的，如字符串、数字、元组
"""
print("-------------------------字典的创建---------------------")
dict1 = {}

print(dict1)

dict2 = dict()

print(dict2)

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print(dict3)

dict4 = dict(name = "赵四" , age = 18 , gender = "male")

print(dict4)

dict5 = dict([("name","赵四"),("age","18"),("gender","male")])

print(dict5)

squares = {x: x**2 for x in range(4)} # 通过字典推导式
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9}