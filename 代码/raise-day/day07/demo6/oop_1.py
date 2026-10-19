"""
    方法重写 子类中定义和父类声明完全相同的方法
    方法名相同 参数相同  满足这些情况 属于子类重写了父类的方法
    比如 我们重写的 __str__函数 __init__函数等等
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

    def print_info(self):
        print("strain:", self.strain)
        super().print_info()


    pass

class Penguin(Pet):
    def __init__(self,name,health,love,sex):
        super().__init__(name,health,love)
        self.sex = sex

    def print_info(self):
        print("sex:",self.sex)
        super().print_info()
    pass


dog1 = Dog("大黄",100,100,"金毛")
dog1.print_info()

print("*" * 50)

p1 = Penguin("大白",100,100,"雌性")
p1.print_info()
