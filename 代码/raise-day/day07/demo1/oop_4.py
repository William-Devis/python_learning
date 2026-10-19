"""
    动态的添加普通方法
"""

class Person:
    pass

def eat():
    print("eat")

p1 = Person()
p1.eat_fuc = eat
p1.eat_fuc()
print(p1.__dict__)

