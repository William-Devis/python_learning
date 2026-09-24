"""
    强制类型转换 float函数
    将传入的数据转换为浮点数
"""

s1 = "11.5"
f1 = float(s1)
print(f1)
print(type(f1))

print("*" * 50)

print(float("3E5"))

print("*" * 50)

# nan 或者 Nan : not a number 不是一个数值

print(float("nan"))
print(float("NaN"))

# inf 或者 infinity
print(float("inf"))
print(float("infinity"))

# print(float("abc")) 报错 并非支持所有字符串