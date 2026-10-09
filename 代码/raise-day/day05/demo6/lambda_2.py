"""
    lambada主要作用 用于处理数据的 是一种语法简洁的优化方式
    使用lambda处理数据
"""
from functools import reduce

# list1 = [2,1,4,6,3]
# list1.sort(reverse=True)
# print(list1)
# print(sorted(list1,reverse=True)) 排序操作 reverse = True 表示降序


person_list = [
    {"name": "jack", "age": 21, "address": "深圳"},
    {"name": "jeery", "age": 11, "address": "深圳"},
    {"name": "tom", "age":35, "address": "广州"},
    {"name": "john", "age": 25, "address": "广州"},
    {"name": "Lily", "age": 55, "address": "北京"},
]

print("---------------------------sorted函数 排序---------------------------------")
# 按照年龄升序或者降序排序 reverse=True 表示降序
print(sorted(person_list,key=lambda p : p["age"],reverse=True))

print(sorted(person_list,key=lambda p : p["name"],reverse=True))

print("---------------------------map函数 映射---------------------------------")
# 呈现每个人姓名的大写形式

print(list(map(lambda p: p["name"].upper(), person_list)))

print("---------------------------filter函数 过滤---------------------------------")
# 查找地址为深圳的人
print(list(filter(lambda p: p["address"] == "深圳", person_list)))

# 查找未成年的人
print(list(filter(lambda p: p["age"] < 18, person_list)))

print("---------------------------reduce函数 合并操作---------------------------------")

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))

# 统计列表中所有人的年龄综合
# print(reduce(lambda p1, p2: p1["age"] + p2["age"], person_list)) # 这里报错 因为年龄相加之后 无法直接赋值给某个字典对象

person_list = [
    {"name": "jack", "age": 21, "address": "深圳"},
    {"name": "jeery", "age": 11, "address": "深圳"},
    {"name": "tom", "age":35, "address": "广州"},
    {"name": "john", "age": 25, "address": "广州"},
    {"name": "Lily", "age": 55, "address": "北京"},
]

print(reduce(lambda p1, total_age: p1["age"] + total_age, person_list))






