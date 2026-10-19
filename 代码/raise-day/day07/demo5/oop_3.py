"""
    单继承条件下方法的查找机制  MRO Method Resolution Order

    P Property 属性
    F Filed  属性

"""

class Animal:
    # def __str__(self):
    #     return "Animal类中的__str__函数"
    pass


class Pet(Animal):
    # def __str__(self):
    #     return "Pet类中的__str__函数"
    pass

class Dog(Pet):
    def __str__(self):
        return "Dog类中的__str__函数" + super().__str__()

    pass

d1 = Dog()
print(Dog.__mro__)
print(d1)
print(d1.__str__())
