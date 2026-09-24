"""
    字典的删除和常用函数
"""

print("-------------------------删除元素---------------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

del dict1 ["name"]
print(dict1)

print("-------------------------pop函数---------------------")

# 获取元素 并且删除
dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print(dict1.pop("name"))

print(dict1)

print("-------------------------clear函数---------------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

dict1.clear()

print(dict1)

print("-------------------------update函数---------------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

dict2 = {"a" : "A" , "b" : "B" ,"c" : "C"}

dict1.update(dict2) # 更新内容到dict1中去

print(dict1)
print(dict2)

print("-------------------------setdefault函数---------------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print(dict1.setdefault("name")) # 如果存在 则直接获取
dict1.setdefault("city","深圳") # 如果不存在 则添加并且获取
print(dict1)

print("-------------------------copy函数---------------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

dict2 = dict1.copy()

print(dict2)