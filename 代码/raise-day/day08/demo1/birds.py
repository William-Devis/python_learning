"""
    birds模块 本模块中书写一个父类 及其三个子类
    父类中书写各个子类共有的信息
    子类中书写独有的信息

    继承：
        1.提高代码的重用性
        2.统一程序结构
"""

class Birds:
    """
        此类属于所有鸟类的父类
        属性：名字 颜色 技能描述
    """
    def __init__(self,name,color,skill):
        self.name = name
        self.color = color
        self.skill = skill

    def fly(self):
        print(f"{self.name}在飞……")

    def call(self):
        print(f"{self.name}发出叫声")

    def use_skill(self):
        print(f"{self.name}使用技能:{self.skill}")


class RedBird(Birds):
    """
        红鸟 如果没有额外的单独的属性 可以不用书写__init__函数了 因为默认使用父类的
    """

    def fly(self):
        super().fly()
        print(f"{self.name}以稳定的速度飞行")

    def call(self):
        print(f"{self.name}发出ji~ji~ji的叫声")


class YellowBird(Birds):
    """
        黄鸟
    """

    def fly(self):
        super().fly()
        print(f"{self.name}以飞快的速度飞行")


    def call(self):
        super.call()
        print(f"{self.name}发出ga~ga~ga的叫声")



class BlueBird(Birds):
    """
        蓝鸟
    """

    def fly(self):
        super().fly()
        print(f"{self.name}以火箭的速度飞行")

    def call(self):
        super.call()
        print(f"{self.name}发出jiu~jiu~jiu的叫声")















