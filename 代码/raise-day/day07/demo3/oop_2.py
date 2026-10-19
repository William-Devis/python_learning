"""
    方法公开：给每个属性提供公开的用于设置属性值  setter  以及 获取属性值的方法 getter
"""

class Person:
    def __init__(self,name,age,sex):
        self.set_name(name) # 这里继续复用我们写好的setter操作  调用对应的 set方法
        self.set_age(age)  # 这里继续复用我们写好的setter操作  调用对应的 set方法
        self.set_sex(sex)  # 这里继续复用我们写好的setter操作  调用对应的 set方法

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self,age):
        if 1 <= age <= 120:
            self.__age = age
        else:
            print("年龄赋值不合法，使用默认值18岁")
            self.__age = 18

    def get_age(self):
        return self.__age


    def set_sex(self,sex):
        if sex == "男" or sex == "女":
            self.__sex = sex
        else:
            print("性别错误，使用默认值：男")
            self.__sex = "男"


    def get_sex(self):
        return self.__sex

    pass

p1 = Person("赵四",-20,"男")
print(p1.get_name())
print(p1.get_age())
print(p1.get_sex())

p1.set_name("abc")
p1.set_age(-888)
p1.set_sex("hello world")

print(p1.get_name())
print(p1.get_age())
print(p1.get_sex())






