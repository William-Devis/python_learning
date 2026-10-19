"""
    删除属性和方法
    回顾删除操作：del 目标.内容名
"""

class Person:
    home = "地球"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print("个人信息介绍",self.name,self.age)

    pass

print(Person.home)

del Person.home

# print(Person.home) # 报错 不存在了 因为已经删除了

p1 = Person("赵四",20)
print(p1.name)
print(p1.age)
p1.show()

del p1.age
del p1.name
# print(p1.age) 上方已经删除 这里无法访问
# print(p1.name)上方已经删除 这里无法访问


p2 = Person("赵四",20)
print(p2.name)
print(p2.age)


print(Person.__dict__) # 可以看到 show函数位于Person类的命名空间 字典中

# del Person.show # 虽然是实例方法 但是属于类 维护在类的命名空间中

# delattr(Person,"show") 这种写法和上方的写法 作用相同

p2.show()






