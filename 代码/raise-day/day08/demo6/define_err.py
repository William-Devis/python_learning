"""
    当Python提供的异常不能满足我们的开发需求 这时 我们需要自定义异常
    自定义异常的步骤：
        编写异常类 继承异常父类即可

    关于异常的类名：
        1.必须一Error单词结尾 通过名字展示出来非普通类
        2.名字尽量简明扼要
"""

class AgeRangeError(Exception):
    pass


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
            raise AgeRangeError("年龄必须在1~120之间")

try:
    s1 = Student("赵四",123)
except AgeRangeError as e:
    print(e)

print("程序结束")

