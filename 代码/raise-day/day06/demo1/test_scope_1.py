"""
    L （Local） 局部作用域
    E （Enclosing）嵌套作用域 闭包函数外的函数中
    G （Global） 全局作用域
    B （Built-in） 内建作用域 Python提供好的
"""


# len = "Global : 全局作用域的变量len"

def func2():
    # len = "Enclosing : 嵌套作用域的变量len"
    def func1():
        # len = "Local : 局部作用域的变量len"
        print(len)
        # print(a) 如果四个范围都查找不到 就报错了
    func1()

func2()




