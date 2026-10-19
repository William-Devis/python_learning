"""
    Python中的封装标准写法为 通过装饰器实现的

    @property  使用此装饰器修饰获取属性值的方法  即getter方法
    @属性名.setter   使用此装饰器修饰设置属性值的方法  即setter方法

    使用以上装饰器修饰函数之后 函数将可以以属性的方式进行访问  (本身函数就是类中的属性)



"""

class Person:
    @property
    def eat(self):
        print("eat函数执行了",self.__class__.__name__)
        return "abc"

    pass

p1 = Person()
p1.eat
# p1.eat() 加了@property装饰器以后 不允许再像普通函数一样调用


