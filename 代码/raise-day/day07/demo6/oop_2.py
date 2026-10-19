"""
    多继承下 方法查找机制  MRO

    子类创建对象 会默认调用父类中的__init__函数

"""

class Person:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name}在吃东西")
    pass

class YellowRace(Person):
    # def eat(self):
    #     print(f"{self.name}黄种人吃饭方式……")
    pass

class BlackRace(Person):
    def eat(self):
        print(f"{self.name}黄种人用手抓")
    pass

class WhiteRace(Person):
    def eat(self):
        print(f"{self.name}黄种人用刀叉吃饭")
    pass

class Chinese(Person):
    # def eat(self):
    #     print(f"{self.name}中国人使用筷子吃饭")
    pass

class Student(Chinese,YellowRace):
    def eat(self):
        super().eat()
    pass

s1  = Student("赵四")
s1.eat()





