"""
    以标准的书写方式 实现封装
        函数名必须和属性名一致
        @property 加在用于获取属性值的函数上方
        @属性名.setter 加在用于设置属性值的函数上方


    Python这样设计 其实是为了简化开发 封装了以后 还可以像没有封装一样书写代码

    属性声明在哪里？
    因为在init函数中 已经没有声明属性了 而是调用对应属性的setter方法 所以在setter方法执行的时候
    临时声明属性 并且给属性赋值
"""

class Person:
    def __init__(self,name,age,sex):
        self.name = name # 这里将调用setter函数
        self.age = age # 这里将调用setter函数
        self.sex = sex # 这里将调用setter函数

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if 1 <= age <= 120:
            self.__age = age
        else:
            print("年龄赋值不合法，使用默认值18岁")
            self.__age = 18

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self,sex):
        if sex == "男" or sex == "女":
            self.__sex = sex
        else:
            print("性别错误，使用默认值：男")
            self.__sex = "男"
    pass

p1 = Person("赵四",-20,"你好")

# p1.age = -999

print(p1.age)





