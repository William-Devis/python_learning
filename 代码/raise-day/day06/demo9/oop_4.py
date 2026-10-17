"""
    实例方法 类方法 静态方法

    如果我们没有显式定义init函数 那么Python解释器自动帮我添加一个 无参的(只有一个参数self) init函数
"""

class Person:
    home = "earth"

    def __init__(self):
        # print("init函数执行了")
        pass

    @classmethod
    def test_cls_method(cls):
        print(cls.home)

    @staticmethod
    def test_static_method():
        print("自定义的静态方法")
        Person.test_static_method1()

    @staticmethod
    def test_static_method1():
        print("自定义的静态方法")
    

Person.test_cls_method()
Person.test_static_method()

p1 = Person()
p1.test_cls_method()
p1.test_static_method()