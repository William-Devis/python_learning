"""
    集合的常用操作
"""

print("-----------------set添加操作----------------")

set1 = {1,2.3,4,5,6}

set1.add(7) # 添加元素之前 是会检查是否有重复项 有则不添加

print(set1)

set1.add(5)

print(set1)

print("-----------------set删除操作----------------")

set1 = {1,2.3,4,5,6}

set1.remove(4)

print(set1)

print("-----------------set成员运算符操作----------------")

print(1 in set1)
print(2 in set1)
print(8 in set1)

print("-----------------set len函数----------------")

set1 = {1,2,3,4,5,6}

print(len(set1))

print("-----------------max min sum操作----------------")

set1 = {1,2,3,4,5,6}
print(max(set1))
print(min(set1))
print(sum(set1))

set2 = {"a","b","c","d","e","f"}
print(set2)
print(max(set2))
print(min(set2))
# print(sum(set2)) 无法求和计算
