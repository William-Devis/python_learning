"""
    列表操作
"""

print("----------------列表的添加操作----------------")

list1 = [11, 22, 33, 44, 55]

list1.append(666)

print(list1)

list1.append([333, 444, 555]) # 添加的是一个列表 依然作为一个元素处理

print(list1)

list1.extend([5,7,9,0]) # 扁平化处理

print(list1)

print("----------------列表的添加操作----------------")

list2 = [11, 2, 24, 4, 55]

# 默认升序 修改原列表 没有返回值 如果要接收 只能得到一个None
# 因为Python中 没有返回值的函数 返回值为None
list.sort(list2) # 原地修改

print(list2)

list2 = [11, 2, 24, 4, 55]

list.sort(list2,reverse=True) # 这种操作属于降序操作

print(list2)