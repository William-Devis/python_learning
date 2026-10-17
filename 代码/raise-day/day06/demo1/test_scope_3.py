"""
    nonlocal 关键字 表示不使用默认作用范围 而使用嵌套函数范围的数据
    使用nonlocal必须有嵌套函数 否则报错
"""


def outer():
    a = 100
    def inner():
        nonlocal a # 表示使用外层嵌套函数中的a
        a = 200
        print(a)
    inner()
    print(a)


outer()


def func1():
    nonlocal a # 报错 因为func1函数不存在外层嵌套函数
    print(a)

func1()
