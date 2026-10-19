"""
    添加实例方法
    必须使用types模块中的函数 MethodType(函数名,对象名)
"""

import types

class Person:
    def __init__(self,name):
        self.name = name
    pass

def eat(self):
    print(f"{self.name}at eating")

p1 = Person("赵四")

print(p1)

# 因为实例方法 必须有self参数 而self必须指向某一个实例对象
# 所以我们通过MethodType() 指定了函数对象 以及 函数必须指向Person对象 即p1
p1.eat_func = types.MethodType(eat,p1)
p1.eat_func()
print(p1.__dict__)


p2 = Person("赵四")
print(p2.__dict__)





