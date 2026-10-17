"""
    面向对象
    人类
        特征-属性：姓名 年龄 性别 身高 体重 爱好 地址 学历……
        行为-方法：吃饭 睡觉 做运动 学习

"""


class Person:
    home = "earth"
    def __init__(self,name,age,gender,height,weight):
        print("__init__函数被调用了")
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def __new__(cls, *args, **kwargs):
        print("__new__函数被调用了")
        print(Person is cls)
        return object.__new__(cls) # 调用父类的方法


    def eat(self):
        print(f"{self.name}在吃饭")

    def sleep(self):
        print(f"{self.name}在睡觉")

    def sport(self):
        print(f"{self.name}在做运动")





# 通过类创建对象 格式 类名()
p1 = Person("赵四",20,"男",175.5,70.5)


# 通过对象访问属性
# 格式 对象名.属性名
print(p1)
print(p1.name)
print(p1.age)
print(p1.gender)
print(p1.height)
print(p1.weight)


# 通过对象访问方法 行为
# 格式 通过对象名.方法名 访问

p1.sleep()
p1.eat()
p1.sport()

print("---------------------------------------------------------------------------------")


p2 = Person("大拿",22,"男",178,88)

print(p2)
print(p2.name)
print(p2.age)
print(p2.gender)
print(p2.height)
print(p2.weight)

p2.eat()
p2.sleep()
p2.sport()




