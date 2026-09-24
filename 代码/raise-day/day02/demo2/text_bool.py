"""
    因为C语言中是没有布尔类型的 使用1或者0来表示真或者假

    而Python延续了这个规则Python中的bool 类型 True 也可理解为1   False理解为0

    True 以及 False 被Python设计为全局单个对象 Global Single Object

    即整个Python进程中 所有的True都是一个对象  所有的False也是一个对象

    ==比较值 值相同 地址值未必相同

    is比较地址值 地址值相同 值一定相同
"""
from stringprep import b3_exceptions

a = True
b = True
print(a)
print(b)
print(type(a))
print(type(b))

# == 用于比较左右两边值是否相同
print(a == 1)
print(b == 0)
print(a + 1)

# is 严格比较地址 即判断内存中是否属于同一个对象
print(a is 1)
print(b is 0)

print("*" * 100)

b1 = True
b2 = True
b3 = True
print(b1 == b2) # 比较值
print(b1 is b2) # 比较内存中的地址
print(b1 is b3) # 比较内存中的地址
print(b2 is b3) # 比较内存中的地址

print("*" * 100)
b1 = False
b2 = False
b3 = False
print(b1 == b2) # 比较值
print(b1 is b2) # 比较内存中的地址
print(b1 is b3) # 比较内存中的地址
print(b2 is b3) # 比较内存中的地址
