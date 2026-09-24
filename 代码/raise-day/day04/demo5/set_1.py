"""
    集合常用函数
"""

print("-----------------pop函数 随机取数据----------------")

set1 = {1,2,3,4,5,6}

print(set1.pop())

set2 = {"abc","hello","text", "a","b","c"}

print(set2.pop())

set3 = set()

# print(set3.pop()) # 集合为空 不能使用pop，会报错

print("-----------------clear函数 清空集合----------------")

set1 = {1,2,3,4,5,6}

set1.clear()

print(set1)

print("-----------------求差集 difference----------------")

# difference 执行完以后会得到一个新的集合
set1 = {1,2,3,4}
set2 = {3,4,5,6}

diff_set1 = set1.difference(set2)

print(diff_set1)

diff_set2 = set2.difference(set1)

print(diff_set2)

print(set1)
print(set2)

print("-----------------求差集 difference_update----------------")
# 原地修改

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set1.difference_update(set2)

print(set1)
print(set2)

print("*" * 20)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set2.difference_update(set1)
print(set1)
print(set2)

print("-----------------求交集 intersection----------------")

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1.intersection(set2)
print("set3:",set3)

print(set1)
print(set2)
print("*" * 20)

set4 = set2.intersection(set1)
print("set4:",set4)
print(set1)
print(set2)

print("-----------------求交集 &----------------")

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1 & set2
print("set3:",set3)

print("-----------------求交集 |----------------")

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1 | set2
print("set3:",set3)

print("-----------------求差集 - ----------------")
set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1 - set2
print("set3:",set3)

set4 = set2 - set1
print("set4:",set4)

# print(set1 + set2) 不能加 否则报错
# print(set1 / set2) 不能除 否则报错

print("-----------------isdisjoint 判断是否没有交集 - ----------------")

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.isdisjoint(set2))

print("-----------------issubset 判断是否是子集 -----------------")

set1 = {3,4}
set2 = {3,4,5,6}

print(set2.issubset(set1))

print("-----------------copy 拷贝集合 -----------------")

set2 = {3,4,5,6}

set3 = set2.copy()

print("set3:",set3)