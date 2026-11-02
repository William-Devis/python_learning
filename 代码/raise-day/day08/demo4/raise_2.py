"""
    raise的使用
"""

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if 1 <= age <= 120:
            self.__age = age
        else:
            raise ValueError("年龄必须在1~120之间")


try:
    s1 = Student("赵四",130)
except ValueError as e:
    print(e)


print("程序结束")




