## day07 类中动态添加信息   封装 继承 多态

### 1. 命名空间

> __ dict __ 属性 属于命名空间 用于保存当前对象包含的各种内容 类 函数 变量 等等
>
> ​	类名.__ dict __
>
> ​	对象名.__ dict __ 
>
> globals() 用于查看当前模块包含了哪些内容

```python
"""
    面向对象：对象创建的过程
    万物皆对象：模块属于对象 类属于对象 函数 属性 都属于对象


    __dict__ 属性 属于命名空间 用于保存当前对象包含的各种内容 类 函数 变量 等等
    globals() 用于查看当前模块包含了哪些内容


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







```

### 2. 对象创建过程

>  面向对象：对象创建的过程
>
> 万物皆对象：模块属于对象 类属于对象 函数 属性 都属于对象
>
> python中创建对象 全部是通过顶级父类object类创建的
>
> 因为只有顶级父类才有权限访问底层的C语言代码 开辟内存空间

> 创建对象 是通过__new__函数 并且将对象返回给我们
>
> Python解释器将对象传递给__init__函数 负责给对象添加属性
>
> __ init __函数并没有返回值 也无法添加返回值 因为它只负责加工对象

```python
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
```

### 3. 动态添加信息

> 给类动态的添加信息 我们自己很少写 但是框架底层会大量的使用到
>
> 所以 我们必须知道 Python是支持这种操作的

#### 3.1 添加变量

```python
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

```

#### 3.2 添加普通方法

```python
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


```

#### 3.3 添加实例方法

```python
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

```

#### 3.4 添加类和静态方法

```python
"""
    动态添加类方法和静态方法
    类方法第一个参数为 cls  即 class 可以使用装饰器 @classmethod
    静态方法没有必须参数 必须使用装饰器@staticmethod
"""

class Person:
    pass

@classmethod
def f1(cls):
    print("类方法f1",cls.__name__)

@staticmethod
def f2():
    print("静态方法f2")


Person.get_f1 = f1
Person.get_f2 = f2
Person.get_f1()
Person.get_f2()


```

#### 3.5 删除属性和方法

> 删除属性和方法
>
> 回顾删除操作：del 目标.内容名

```python
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
```

#### 3.6 __ slots __特殊变量

```python
"""
    __slots__ 特殊的属性 可以用于规定类中可以添加哪些内容
"""

class Person:
    __slots__ = ("name","age","eat")
    pass


def eat():
    print("eat")
p1 = Person()

p1 = Person()
p1.name = "赵四"
p1.age = 30
p1.eat = eat
p1.eat()


# p1.sex = "男" 这里报错 因为元组中没有指定 sex 所以不能添加

```



### 4. 封装

> 封装介绍：面向对象三大特征之一
> ​    属性私有：将所有的属性隐藏起来 不让外界直接访问
> ​    方法公开：给每个属性提供公开的用于设置属性值  setter  以及 获取属性值的方法 getter
>
> 名称之前加一个下划线 _name 表示声明为私有的 但是不具备约束力
> 名称之前加两个下划线 __name 表示声明为私有的 是通过改名字的机制来不让我们直接访问的
> 所以加上对应的前缀名 依然还可以访问

```python
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



```

> 方法公开：给每个属性提供公开的用于设置属性值  setter  以及 获取属性值的方法 getter

```python
"""
    方法公开：给每个属性提供公开的用于设置属性值  setter  以及 获取属性值的方法 getter
"""

class Person:
    def __init__(self,name,age,sex):
        self.set_name(name) # 这里继续复用我们写好的setter操作  调用对应的 set方法
        self.set_age(age)  # 这里继续复用我们写好的setter操作  调用对应的 set方法
        self.set_sex(sex)  # 这里继续复用我们写好的setter操作  调用对应的 set方法

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self,age):
        if 1 <= age <= 120:
            self.__age = age
        else:
            print("年龄赋值不合法，使用默认值18岁")
            self.__age = 18

    def get_age(self):
        return self.__age


    def set_sex(self,sex):
        if sex == "男" or sex == "女":
            self.__sex = sex
        else:
            print("性别错误，使用默认值：男")
            self.__sex = "男"


    def get_sex(self):
        return self.__sex

    pass

p1 = Person("赵四",-20,"男")
print(p1.get_name())
print(p1.get_age())
print(p1.get_sex())

p1.set_name("abc")
p1.set_age(-888)
p1.set_sex("hello world")

print(p1.get_name())
print(p1.get_age())
print(p1.get_sex())

```

### 5.Python封装标准实现

> Python中的封装标准写法为 通过装饰器实现的
>
> @property  使用此装饰器修饰获取属性值的方法  即getter方法
> @属性名.setter   使用此装饰器修饰设置属性值的方法  即setter方法
>
> 使用以上装饰器修饰函数之后 函数将可以以属性的方式进行访问  (本身函数就是类中的属性)

```python
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



```

> 以标准的书写方式 实现封装
> ​    函数名必须和属性名一致
> ​    @property 加在用于获取属性值的函数上方
> ​    @属性名.setter 加在用于设置属性值的函数上方
>
>
> Python这样设计 其实是为了简化开发 封装了以后 还可以像没有封装一样书写代码
>
> 属性声明在哪里？
>
> ​	因为在init函数中 已经没有声明属性了 而是调用对应属性的setter方法 所以在setter方法执行的时候
>
> ​	临时声明属性 并且给属性赋值

```python
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

```

### 6. 继承

> 继承
>
> 观察一下两个类 发现存在一些相同的属性 以及 相同的函数
>
> 这些相同的信息如果重复书写 非常麻烦 啰嗦 代码冗余
>
> 我们应该将这些重复的信息抽取出来 编写在一个父类中 子类中书写各个子类独有的信息

```python
"""
    继承
    观察一下两个类 发现存在一些相同的属性 以及 相同的函数
    这些相同的信息如果重复书写 非常麻烦 啰嗦 代码冗余
    我们应该将这些重复的信息抽取出来 编写在一个父类中 子类中书写各个子类独有的信息
"""
class Dog:
    def __init__(self,name,health,love,strain):
        self.name = name
        self.health = health
        self.love = love
        self.strain = strain

    def print_info(self):
        print("name:",self.name)
        print("health:",self.health)
        print("love:",self.love)
        print("strain:",self.strain)
    pass

class Penguin:
    def __init__(self,name,health,love,sex):
        self.name = name
        self.health = health
        self.love = love
        self.sex = sex

    def print_info(self):
        print("name:",self.name)
        print("health:",self.health)
        print("love:",self.love)
        print("sex:",self.sex)
    pass
```

> 使用继承优化代码
>
> 继承的核心思想：子类与父类是is-a的关系 子类是父类
> 子类是父类 表示子类必须属于父类表示的这一范围的事物  才能使用继承 否则不能用继承

```python
"""
    使用继承优化代码

    继承的核心思想：子类与父类是is-a的关系 子类是父类
    子类是父类 表示子类必须属于父类表示的这一范围的事物  才能使用继承 否则不能用继承

"""
class Pet:
    def __init__(self,name,health,love):
        self.name = name
        self.health = health
        self.love = love

    def print_info(self):
        print("name:", self.name)
        print("health:", self.health)
        print("love:", self.love)

    pass


class Dog(Pet):
    def __init__(self,name,health,love,strain):
        self.strain = strain
        super().__init__(name,health,love)
    pass

class Penguin(Pet):
    def __init__(self,name,health,love,sex):
        super().__init__(name,health,love)
        self.sex = sex
    pass

dog1 = Dog("大黄",100,100,"金毛")
dog1.print_info()
print("strain:",dog1.strain)

print("*" * 50)

p1 = Penguin("大白",100,100,"雌性")
p1.print_info()
print("sex:",p1.sex)
```

### 7. 单继承条件下的MRO机制

> 单继承条件下方法的查找机制  MRO Method Resolution Order
>
> P Property 属性
> F Filed  属性

```python
"""
    单继承条件下方法的查找机制  MRO Method Resolution Order

    P Property 属性
    F Filed  属性

"""

class Animal:
    # def __str__(self):
    #     return "Animal类中的__str__函数"
    pass


class Pet(Animal):
    # def __str__(self):
    #     return "Pet类中的__str__函数"
    pass

class Dog(Pet):
    def __str__(self):
        return "Dog类中的__str__函数" + super().__str__()

    pass

d1 = Dog()
print(Dog.__mro__)
print(d1)
print(d1.__str__())

```

### 8. 方法重写

> 方法重写 子类中定义和父类声明完全相同的方法
>
> 方法名相同 参数相同  满足这些情况 属于子类重写了父类的方法
>
> 比如 我们重写的 __str__函数 __init__函数等等

```python
"""
    方法重写 子类中定义和父类声明完全相同的方法
    方法名相同 参数相同  满足这些情况 属于子类重写了父类的方法
    比如 我们重写的 __str__函数 __init__函数等等
"""

class Pet:
    def __init__(self,name,health,love):
        self.name = name
        self.health = health
        self.love = love

    def print_info(self):
        print("name:", self.name)
        print("health:", self.health)
        print("love:", self.love)

    pass


class Dog(Pet):
    def __init__(self,name,health,love,strain):
        self.strain = strain
        super().__init__(name,health,love)

    def print_info(self):
        print("strain:", self.strain)
        super().print_info()


    pass

class Penguin(Pet):
    def __init__(self,name,health,love,sex):
        super().__init__(name,health,love)
        self.sex = sex

    def print_info(self):
        print("sex:",self.sex)
        super().print_info()
    pass


dog1 = Dog("大黄",100,100,"金毛")
dog1.print_info()

print("*" * 50)

p1 = Penguin("大白",100,100,"雌性")
p1.print_info()

```



### 9. 多继承条件下的MRO机制

```python
"""
    多继承下 方法查找机制  MRO

    子类创建对象 会默认调用父类中的__init__函数

"""

class Person:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name}在吃东西")
    pass

class YellowRace(Person):
    # def eat(self):
    #     print(f"{self.name}黄种人吃饭方式……")
    pass

class BlackRace(Person):
    def eat(self):
        print(f"{self.name}黄种人用手抓")
    pass

class WhiteRace(Person):
    def eat(self):
        print(f"{self.name}黄种人用刀叉吃饭")
    pass

class Chinese(Person):
    # def eat(self):
    #     print(f"{self.name}中国人使用筷子吃饭")
    pass

class Student(Chinese,YellowRace):
    def eat(self):
        super().eat()
    pass

s1  = Student("赵四")
s1.eat()






```

### 10.__ init __访问机制

> 子类创建对象 如果本类中没有书写 __ init __ 函数 
>
> 则会默认调用父类中的__ init __函数

```python
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
```

### 11. 多态

> 多态：同一个事物 因为环境不同 产生不同的结果
>
> 给宠物系统添加功能 ，每个宠物可以去医院看病
>
> 多态的要求：必须有继承 必须有方法重写

```python
"""
    多态：同一个事物 因为环境不同 产生不同的结果

    给宠物系统添加功能 ，每个宠物可以去医院看病

    多态的要求：必须有继承 必须有方法重写

"""

class Pet:
    def __init__(self,name,health,love):
        self.name = name
        self.health = health
        self.love = love

    def print_info(self):
        print("name:", self.name)
        print("health:", self.health)
        print("love:", self.love)


    def cure(self):
        print(f"{self.name}在看病")
    pass

class Dog(Pet):
    def __init__(self,name,health,love,strain):
        self.strain = strain
        super().__init__(name,health,love)

    def print_info(self):
        print("strain:", self.strain)
        super().print_info()

    def cure(self):
        print(f"{self.name}狗狗看病，吃药，恢复健康值")
        self.health = 100
    pass

class Penguin(Pet):
    def __init__(self,name,health,love,sex):
        super().__init__(name,health,love)
        self.sex = sex

    def print_info(self):
        print("sex:", self.sex)
        super().print_info()

    def cure(self):
        print(f"{self.name}企鹅看病，打针，恢复健康值")
        self.health = 100
    pass

class Master:
    """
        这个类的主要作用：带着宠物去看病
    """
    def __init__(self,name):
        self.name = name

    def to_hospital_dog(self,dog):
        print(f"{self.name}带着{dog.name}去医院")
        dog.cure()

    def to_hospital_penguin(self,penguin):
        print(f"{self.name}带着{penguin.name}去医院")
        penguin.cure()

    # 以上的写法 针对两种宠物 书写了两个方法 分别实现看病效果
    # 如果后续有更多的宠物 则还需要继续编写新的方法 太啰嗦 太麻烦
    # 开闭原则 ： 扩展开放  修改关闭
    # 我们应该编写一个方法 实现给所有的宠物看病  现存的 以及 未来新增的


    def to_hospital(self,pet):
        print(f"{self.name}带着{pet.name}去医院")
        pet.cure()


    pass

m1 = Master("赵四")

dog1 = Dog("大黄",20,100,"金毛")

m1.to_hospital_dog(dog1)

p1 = Penguin("大白",20,100,"雄性")

m1.to_hospital_penguin(p1)




```

> 使用多态优化宠物看病操作

```python
"""
    多态：同一个事物 因为环境不同 产生不同的结果
    给宠物系统添加功能 ，每个宠物可以去医院看病
    多态的要求：必须有继承 必须有方法重写

    使用多态优化宠物看病操作

"""

class Pet:
    def __init__(self,name,health,love):
        self.name = name
        self.health = health
        self.love = love

    def print_info(self):
        print("name:", self.name)
        print("health:", self.health)
        print("love:", self.love)


    def cure(self):
       pass
    pass

class Dog(Pet):
    def __init__(self,name,health,love,strain):
        self.strain = strain
        super().__init__(name,health,love)

    def print_info(self):
        print("strain:", self.strain)
        super().print_info()

    def cure(self):
        print(f"{self.name}狗狗看病，吃药，恢复健康值")
        self.health = 100
    pass

class Penguin(Pet):
    def __init__(self,name,health,love,sex):
        super().__init__(name,health,love)
        self.sex = sex

    def print_info(self):
        print("sex:", self.sex)
        super().print_info()

    def cure(self):
        print(f"{self.name}企鹅看病，打针，恢复健康值")
        self.health = 100
    pass

class Cat(Pet):
    def __init__(self, name, health, love, fur_color):
        super().__init__(name, health, love)
        self.fur_color = fur_color


    def cure(self):
        print(f"{self.name}猫咪看病，输液，恢复健康值")
        self.health = 100

class Master:
    """
        这个类的主要作用：带着宠物去看病
    """
    def __init__(self,name):
        self.name = name

    # def to_hospital_dog(self,dog):
    #     print(f"{self.name}带着{dog.name}去医院")
    #     dog.cure()
    #
    # def to_hospital_penguin(self,penguin):
    #     print(f"{self.name}带着{penguin.name}去医院")
    #     penguin.cure()

    # 以上的写法 针对两种宠物 书写了两个方法 分别实现看病效果
    # 如果后续有更多的宠物 则还需要继续编写新的方法 太啰嗦 太麻烦
    # 开闭原则 ： 扩展开放  修改关闭
    # 我们应该编写一个方法 实现给所有的宠物看病  现存的 以及 未来新增的


    def to_hospital(self,pet):
        print(f"{self.name}带着{pet.name}去医院")
        pet.cure()


    pass

m1 = Master("赵四")

dog1 = Dog("大黄",20,100,"金毛")

m1.to_hospital(dog1)

p1 = Penguin("大白",20,100,"雄性")

m1.to_hospital(p1)

c1 = Cat("小红",100,100,"绿色")

m1.to_hospital(c1)



```

