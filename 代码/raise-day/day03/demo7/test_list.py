"""
    list属于列表 属于有序序列
    下标从0开始 往后逐个递增 同时也可以使用-1表示最后一个元素 往前逐个递减
"""

list1 = [100,200,300,400,500,600]
print(list1)
print(type(list1))
print("--------------正序访问---------------")
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])
# print(list1[6]) 访问不存在的下标 会导致程序中断 报错  IndexError: List index out of range
print("--------------倒序访问---------------")

print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])
print(list1[-5])
print(list1[-6])

print("--------------切片操作---------------")

list2 = list1[:]
print(list2)
# 下标包括1 不包括3
print(list2[1:3])

print(list2[2:])

print(list2[:4])

print(list2[2:-1]) # 从2下标 到-1下标 不包括-1下标元素

print(list2[::-1])

print("--------------添加操作--------------")

print(list2)

list2.append(999)
print(list2)

list2.insert(0,666)

print(list2)

print("程序结束")