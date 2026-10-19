"""
    给类动态的添加信息 我们自己很少写 但是框架底层会大量的使用到
    所以 我们必须知道 Python是支持这种操作的
"""

class Person:

    pass


p1 = Person() #
print(p1)
p1.name = "赵四"
p1.sex = "男"
p1.height = 188
p1.area = 200
print(p1.name)

p2 = Person()
print(p2)
# print(p2.name) # 添加给p1对象的属性 p2中是不存在的 因为每个对象单独维护一个 字典

print("--------------------------------------------------------------------------")

class Student:
    pass

Student.home = "学校"

s1 = Student()
print(s1)
print(s1.home)

s2 = Student()
print(s2)
print(s2.home)

print(Student.home)








