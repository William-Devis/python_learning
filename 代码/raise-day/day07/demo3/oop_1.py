"""
    封装介绍：面向对象三大特征之一
        属性私有：将所有的属性隐藏起来 不让外界直接访问
        方法公开：给每个属性提供公开的用于设置属性值  setter  以及 获取属性值的方法 getter

    名称之前加一个下划线 _name 表示声明为私有的 但是不具备约束力
    名称之前加两个下划线 __name 表示声明为私有的 是通过改名字的机制来不让我们直接访问的
    所以加上对应的前缀名 依然还可以访问


"""
class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self._age = age
        self.__sex = sex


    pass

p1 = Person("赵四",-199,"你好")
print(p1.name)
print(p1._age) # 正常访问
print(p1._Person__sex) # 这样还可以访问 但是不推荐


