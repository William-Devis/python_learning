"""
    自定义的函数之间 直接调用

    栈 stack 先进后出 后进先出 FILO
    函数执行是要进栈的 栈是一种数据结构 先进栈的 后出栈

"""

def my_func2():
    print("my_func2 开始执行")
    print("my_func2 执行完毕")

def my_func1():
    print("my_func2 开始执行**********")
    my_func2()
    print("my_func2 执行完毕**********")

my_func1()



