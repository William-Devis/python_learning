"""
    __slots__ 特殊的属性 可以用于规定类中可以添加哪些内容
"""

class Person:
    __slots__ = ("name","age","eat")
    pass


def eat():
    print("eat")
p1 = Person()

p1 = Person()
p1.name = "赵四"
p1.age = 30
p1.eat = eat
p1.eat()


# p1.sex = "男" 这里报错 因为元组中没有指定 sex 所以不能添加
