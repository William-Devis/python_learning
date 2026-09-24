"""
    字典的使用
"""

print("---------------------字典的访问----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print(dict3["name"])
print(dict3["age"])
# print(dict3["address"]) # 如果键不存在 会报错

print("---------------------字典的访问 通过 get 函数访问----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male","name" : "小宝"}

print(dict3.get("name"))
print(dict3.get("age"))
print(dict3.get("gender"))
print(dict3.get("address"))
print(dict3.get("address","深圳")) # 如果为None 指定默认值为 “深圳”

print("---------------------字典的访问 添加数据----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male", "name" : "小宝"}

dict3["city"] = "深圳"

print(dict3)

print("---------------------字典的访问 修改数据----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

dict3["name"] = "小宝"

print(dict3)

print("---------------------字典的访问 查看是否包含某个键----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print("name" in dict3)
print("赵四" in dict3)

print("---------------------字典的访问 len函数----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print(len(dict3))






