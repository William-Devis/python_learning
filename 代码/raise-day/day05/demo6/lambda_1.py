"""
    lambda 匿名函数 面向函数编程 不关注谁来做 只关注做什么
    ctrl + alt + L 自动格式化对齐代码
"""

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def operation(a,b,func):
    return func(a,b)

print(add)
print(sub)
print(mul)
print(div)

print(operation(1, 2, mul))

print("*" * 50)

operation(1,2,lambda a ,b : a + b)

print(lambda a ,b : a + b)
print(type(lambda a ,b : a + b))











