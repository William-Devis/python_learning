"""
    面向对象
    人类
        特征-属性：姓名 年龄 性别 身高 体重 爱好 地址 学历……
        行为-方法：吃饭 睡觉 做运动 学习

    通过self访问本类中的方法 行为  self.方法名()

    self 表示当前对象 即正在使用的对象
"""


class Person:
    home = "earth"
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_name(self):
        print(f"人的姓名是：{self.name}")

    def print_age(self):
        print(f"人的年龄是：{self.age}")

    def print_gender(self):
        print(f"人的性别是：{self.gender}")

    def print_info(self):
        self.print_name()
        self.print_age()
        self.print_gender()

p1 = Person("赵四",20,"男")
p1.print_info()




