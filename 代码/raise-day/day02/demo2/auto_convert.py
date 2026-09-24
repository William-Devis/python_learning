"""
    自动类型转换 我们在使用不同的类型数据进行计算 会涉及到自动类型转换
    对于整数和浮点数进行计算 结果会自动转换为浮点数类型
"""

a = 10
b = 2.5
result1 = a + b
print(result1)
print(type(result1))

c = 10
d = 1
result2 = c / d
print(result2)
print(type(result2))


# 跟Java语言不同 Python中不允许数值和字符直接加法计算
e = 10
f = "hello"
# 错误(异常)会导致程序中断 后续我们可以通过异常处理机制 来捕获异常
print(e + f) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("程序结束")