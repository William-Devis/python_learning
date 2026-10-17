"""
    global 关键字 显示声明使用全局作用域的变量 而非默认作用域
"""

list1 = [1,2,3]

def func1():
    list1[0] = 666 # 对于可变数据类型 可以直接修改数据

func1()
print(list1)

num = 100

def func2():
    global num # 显式说明 这里使用的是全局作用域的num 而非默认作用范围
    num = 200
    print(num)

func2()
print(num)












