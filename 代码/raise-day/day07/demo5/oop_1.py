"""
    继承
    观察一下两个类 发现存在一些相同的属性 以及 相同的函数
    这些相同的信息如果重复书写 非常麻烦 啰嗦 代码冗余
    我们应该将这些重复的信息抽取出来 编写在一个父类中 子类中书写各个子类独有的信息
"""
class Dog:
    def __init__(self,name,health,love,strain):
        self.name = name
        self.health = health
        self.love = love
        self.strain = strain

    def print_info(self):
        print("name:",self.name)
        print("health:",self.health)
        print("love:",self.love)
        print("strain:",self.strain)
    pass

class Penguin:
    def __init__(self,name,health,love,sex):
        self.name = name
        self.health = health
        self.love = love
        self.sex = sex

    def print_info(self):
        print("name:",self.name)
        print("health:",self.health)
        print("love:",self.love)
        print("sex:",self.sex)



    pass




