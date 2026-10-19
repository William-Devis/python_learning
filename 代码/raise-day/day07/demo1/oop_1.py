"""



    __dict__ 属性 属于命名空间 用于保存当前对象包含的各种内容 类 函数 变量 等等
    globals() 用于查看当前模块包含了哪些内容

     面向对象：对象创建的过程
    万物皆对象：模块属于对象 类属于对象 函数 属性 都属于对象
    python中创建对象 全部是通过顶级父类object类创建的
    因为只有顶级父类才有权限访问底层的C语言代码 开辟内存空间




"""

class Person:
    """
        这是一个Person类
    """

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print("__new__执行了")
        return object.__new__(cls)

    def running(self):
        print(f"{self.name}run")

    pass

def func():
    print("func")

a = 100
print("模块中的内容：",globals())

print("Person类中的内容：",Person.__dict__)

p1 = Person("赵四",20)
print(p1)
print(p1.name)
print(p1.age)
p1.__dict__["sex"] = "male"

print("p1对象中的内容：",p1.__dict__)

p2 = Person("赵四",20)
print(p2.__dict__)






