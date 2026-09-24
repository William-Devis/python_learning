"""
    元组的使用
    元组是一个不可变的、有序的元素集合。
    不能对元组中的元素进行修改操作。
    元组使用 () 定义，数据之间使用，分隔。
    元组中每个元素都有对应的位置值，称为索引或下标，索引从起始从0开始向后逐个递增，并且末尾从-1开始逐个向前递减。
    元组中元素可以是不同的类型。
    元组的使用方式与列表类似
"""

print("*****************元组的使用 方式基本与list一致***************")
tuple1 = (1,22,33,4,55,6,)

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])
print(tuple1[5])

# print(tuple1[6]) 超出下标范围报错

print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])
print(tuple1[-4])
print(tuple1[-5])
print(tuple1[-6])

print("*****************元组的切片 方式基本与list一致***************")

print(tuple1[0:3])
print(tuple1[0:-2])

