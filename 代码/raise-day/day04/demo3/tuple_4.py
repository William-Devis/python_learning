"""
    tuple基本使用
"""

print("-------------成员运算符的使用--------------")
tuple1 = (1,22,33,4,55,6,)

print(1 in tuple1)
print(2 in tuple1)

print("-------------len函数获取元组中的元素个数--------------")
tuple1 = (1,22,33,4,55,6,)

print(len(tuple1))

print("-------------max min sum 函数用法一致--------------")
tuple1 = (1,22,33,4,55,6,)

print(max(tuple1))
print(min(tuple1))
print(sum(tuple1))

tuple2 = ('a', 'b', 'c', 'd', 'e', '你')
print(max(tuple2))
print(min(tuple2))
# print(sum(tuple2)) 对于元素类型为字符串类型 可以找最大最小值 但是不能求和
