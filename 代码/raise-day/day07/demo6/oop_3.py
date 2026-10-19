"""
    子类创建对象 会默认调用父类中的__init__函数
"""


class Animal:
    def __init__(self):
        print("Animal类中的init函数执行了")
    pass

class Pet(Animal):
    def __init__(self):
        print("Pet类中的init函数执行了")
    pass


print(Pet())