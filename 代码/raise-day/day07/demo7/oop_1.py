"""
    多态：同一个事物 因为环境不同 产生不同的结果

    给宠物系统添加功能 ，每个宠物可以去医院看病

    多态的要求：必须有继承 必须有方法重写

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


    def cure(self):
        print(f"{self.name}在看病")
    pass

class Dog(Pet):
    def __init__(self,name,health,love,strain):
        self.strain = strain
        super().__init__(name,health,love)

    def print_info(self):
        print("strain:", self.strain)
        super().print_info()

    def cure(self):
        print(f"{self.name}狗狗看病，吃药，恢复健康值")
        self.health = 100
    pass

class Penguin(Pet):
    def __init__(self,name,health,love,sex):
        super().__init__(name,health,love)
        self.sex = sex

    def print_info(self):
        print("sex:", self.sex)
        super().print_info()

    def cure(self):
        print(f"{self.name}企鹅看病，打针，恢复健康值")
        self.health = 100
    pass

class Master:
    """
        这个类的主要作用：带着宠物去看病
    """
    def __init__(self,name):
        self.name = name

    def to_hospital_dog(self,dog):
        print(f"{self.name}带着{dog.name}去医院")
        dog.cure()

    def to_hospital_penguin(self,penguin):
        print(f"{self.name}带着{penguin.name}去医院")
        penguin.cure()

    # 以上的写法 针对两种宠物 书写了两个方法 分别实现看病效果
    # 如果后续有更多的宠物 则还需要继续编写新的方法 太啰嗦 太麻烦
    # 开闭原则 ： 扩展开放  修改关闭
    # 我们应该编写一个方法 实现给所有的宠物看病  现存的 以及 未来新增的


    def to_hospital(self,pet):
        print(f"{self.name}带着{pet.name}去医院")
        pet.cure()


    pass

m1 = Master("赵四")

dog1 = Dog("大黄",20,100,"金毛")

m1.to_hospital_dog(dog1)

p1 = Penguin("大白",20,100,"雄性")

m1.to_hospital_penguin(p1)



