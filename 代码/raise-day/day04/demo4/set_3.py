"""
    set其他操作
"""

print("-------------------set遍历操作----------------")

set1 = {1,2,3,4,5,6}

for i in set1:
    print(i)

print("-------------------set遍历操作----------------")
# update函数依然属于添加操作 对比add 支持更多的类型 比如容器类型

set1 = {1,2,3,4,5,6}

set1.add(8)

set1.update({22,44,55,66})

print(set1)

print("-------------------set union操作----------------")

set1 = {1,2,3,4,5,6}

set2 = set1.union({11,22,33}) # 返回新的集合 所以需要接收 原集合不变

print(set1)

print(set2)

print("-------------------remove操作----------------")

set1 = {1,2,3,4,5,6}

set1.remove(1)

print(set1)

# set1.remove(7) # 删除不存在的 会报错

print(set1)

print("-------------------set discard操作----------------")

set1 = {1,2,3,4,5,6}

set1.discard(2)

print(set1)

set1.discard(8) # 这里删除不存在的 不会报错

print(set1)