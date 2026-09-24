"""
    变量的修改 变量中的值是可以改变的   直接重新赋值  即覆盖(改变)了原变量中的值
"""


a = "hello"
a = "world"
print(a)
a = 100
print(a)

b = 5
c = 6
print(b, c)
b, c = c, b # 交换变量的值 直接交换 更加简洁
print(b, c)


# 其他语言中啰嗦的写法 比如 Java
num1 = 100
num2 = 200
temp = num1
num1 = num2
num2 = temp