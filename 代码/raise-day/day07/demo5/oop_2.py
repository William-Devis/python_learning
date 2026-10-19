"""
    使用继承优化代码

    继承的核心思想：子类与父类是is-a的关系 子类是父类
    子类是父类 表示子类必须属于父类表示的这一范围的事物  才能使用继承 否则不能用继承

"""
class Pet:
    def __init__(self,name,health,love):
        self.name = name
        self.health = health
        self.love = love

    def print_info(self):
        print("name:", self.name)
        print("health:", self.health)
        print("love:", self.love)

    pass


class Dog(Pet):
    def __init__(self,name,health,love,strain):
        self.strain = strain
        super().__init__(name,health,love)
    pass

class Penguin(Pet):
    def __init__(self,name,health,love,sex):
        super().__init__(name,health,love)
        self.sex = sex
    pass

dog1 = Dog("大黄",100,100,"金毛")
dog1.print_info()
print("strain:",dog1.strain)

print("*" * 50)

p1 = Penguin("大白",100,100,"雌性")
p1.print_info()
print("sex:",p1.sex)






