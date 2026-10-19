"""
    创建对象 是通过__new__函数 并且将对象返回给我们
    Python解释器将对象传递给__init__函数 负责给对象添加属性
    __init__函数并没有返回值 也无法添加返回值 因为它只负责加工对象
"""

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print("__new__函数执行了")
        return super().__new__(cls)


    def __str__(self):
        return f"Person类__str__函数  {id(self)}  {self.name} {self.age}"
    pass

p1 = Person("赵四",20)
print(p1)