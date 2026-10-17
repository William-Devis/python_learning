"""
    顶级父类object类中的函数
    __str__函数  这个函数属于打印对象默认将调用的魔法函数
    打印一个对象 默认调用此函数 使用父类的实现 返回类型 以及 id值
    我们可以重写这个函数 覆盖父类的实现
    实际工作中的做法：返回当前类名 以及 属性名和属性值

    __repr__() 函数 用于给程序员调试使用 展示真实的数据

    __getattribute__() 属于属性拦截器 访问任何属性都将被此函数拦截
"""


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        用于展示更加美观的结果
        :return:
        """
        return f"Student [name:{self.name}, age:{self.age}]"


    def __repr__(self):
        """
        repr函数主要用于在程序中调试使用
        :return:
        """
        return f"Student [name:{repr(self.name)}, age:{self.age}]"

    def __getattribute__(self, item):
        print(f"{item}属性被访问了")
        return super().__getattribute__(item) # 必须调用父类的方法 否则会报错 出现无穷递归






s1 = Student("赵\t\t四",20)
print(s1.name)
# print(s1.__str__())
# print(s1.__repr__())