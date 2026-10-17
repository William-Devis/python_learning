"""
    类变量：直接书写在类中 属于当前类 不属于任何对象  可以被此类的所有对象共享
      应该使用类名加点的方式访问
    但是也可以通过对象名加点的方式访问 但是不推荐

    实例变量：在__init__函数中定义的变量 属于实例级别的
    必须通过实例(对象)来访问

    实例：instance 对象  创建对象这个操作 也叫实例化

"""

class Person:
    home = "earth"

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("赵四1",20)
print(p1.name, p1.age)

Person.home = "地球"

print(Person.home) # 推荐这样访问
print(p1.home) # 也可以访问 但是不推荐

p2 = Person("赵四2",20)
print(p2.home)
