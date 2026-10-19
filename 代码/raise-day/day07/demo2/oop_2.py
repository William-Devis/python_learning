"""
    动态添加类方法和静态方法
    类方法第一个参数为 cls  即 class 可以使用装饰器 @classmethod
    静态方法没有必须参数 必须使用装饰器@staticmethod
"""

class Person:
    pass

@classmethod
def f1(cls):
    print("类方法f1",cls.__name__)

@staticmethod
def f2():
    print("静态方法f2")


Person.get_f1 = f1
Person.get_f2 = f2
Person.get_f1()
Person.get_f2()

