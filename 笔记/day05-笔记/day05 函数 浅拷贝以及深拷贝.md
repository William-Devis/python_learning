## 函数

### 1. 函数的概念

> 函数即一系列代码指令的集合   用于解决特定的问题   可以反复调用
>     必须先定义 再使用

### 2. 定义格式

~~~python
    def 函数名():
        函数体
~~~

### 3. 调用

> 直接在需要调用的位置书写函数名即可

~~~python
"""
    函数即一系列代码指令的集合   用于解决特定的问题   可以反复调用
    必须先定义 再使用
"""

# 以下代码 虽然可以实现需求 但是书写非常啰嗦 代码存在 冗余
print("床前明月光")

print("--------------")

print("疑是地上霜")

print("--------------")

print("举头望明月")

for _ in range(10):
    print("-",end="")
print()

print("低头思故乡")
for _ in range(10):
    print("-",end="")
print()
~~~

### 4. 参数

> 继续优化：可以让调用者灵活的控制符号数量
>
> 通过参数实现：函数的调用者与函数的定义之间传递的数据 称之为参数
>
> ​	形参：形式参数 函数定义的时候书写的参数 属于形参
> ​       实参：实际参数 函数调用的时候传入的参数 属于实参
>
> 定于了形参以后 必须传入对应个数的实参 除非形参有默认值 否则运行报错

~~~python
"""
    继续优化：可以让调用者灵活的控制符号数量

    通过参数实现：函数的调用者与函数的定义之间传递的数据 称之为参数
        形参：形式参数 函数定义的时候书写的参数 属于形参
        实参：实际参数 函数调用的时候传入的参数 属于实参

    定于了形参以后 必须传入对应个数的实参 除非形参有默认值 否则运行报错
"""

def print_sign(num):
    for _ in range(num):
        print("-", end="")
    print()


print("床前明月光")
print_sign(7)

print("疑是地上霜")
print_sign(10)

print("举头望明月")
print_sign(20)

print("低头思故乡")
print_sign(85)
~~~

> 继续优化：可以让调用者灵活的控制符号数量 以及 符号的类型
>
>  对于函数定义的时候，参数的数量结合具体需求定义即可，没有限制

~~~python
"""
    继续优化：可以让调用者灵活的控制符号数量 以及 符号的类型

    对于函数定义的时候，参数的数量结合具体需求定义即可，没有限制
"""

def print_sign(num,sign):
    for _ in range(num):
        print("-", end="")
    print()


print("床前明月光")
print_sign(7,"A")

print("疑是地上霜")
print_sign(10,"&")

print("举头望明月")
print_sign(2,"hello")

print("低头思故乡")
print_sign(8,"*")
~~~

### 5. 传参规则

> 关于参数的传递细节
>
> 位置参数
>
> 关键字参数
>
> 解包传参

#### 5.1 位置和关键字参数

~~~python
"""
    关于参数的传递细节
        位置参数
        关键字参数
        解包传参
"""

def print_sign(num,sign):
    for _ in range(num):
        print("-", end="")
    print()


print("床前明月光")
print_sign(7,"^") # 位置参数 严格按照位置的顺序传入

print("疑是地上霜")
print_sign(10,"&")

print("举头望明月")
print_sign(sign = "&",num = 10)

print("低头思故乡")
print_sign(8,"*")


# print_sign(num = 8,"*") 不能这样书写 报错 关键字参数必须再位置参数后边
~~~

#### 5.2 解包传参

~~~python
"""
    关于参数的传递细节

        解包传参
"""

def func(a,b,c):
    print(a,b,c)

func(1,2,3)
func(a=1,b=2,c=3)
func(1,2,c=3)

list1 = [2,1,3]
func(*list1)

tuple1 = (2,1,3)
func(*tuple1)

set1 = {2,1,3}
func(*set1) # 实际工作中不用 因为顺序无法保证

# 字典解包传参 其实是为了处理关键字参数
# 所以 字典中的键的名字必须和形参的名字完全一致 对照 数量相同
# 顺序无所谓 因为关键字参数 本身就没有顺序要求
dict1 = {"a":1,"b":2,"c":3}
func(**dict1)
func(b = 2,a = 1,c = 3)
~~~

#### 5.3 可变长参数

~~~python
"""
    可变长参数   以及 默认值参数
"""

def func1(a,*nums):
    print(a,nums)

func1(1,2,3,4,5)
func1(1,2)

# 如果在可变长参数之后还有参数 必须通过关键字参数的方式 进行传递
def func2(a,*num3,b):
    print(a,*num3,b)

func2(1,2,3,4,5,b = 6)
~~~

#### 5.4 默认值参数

~~~python
def func3(a=1,b=True):
    print(a,b)

func3() # 有默认值的参数 可以不传 将使用默认值
func3(2,False) # 也可以传入新的值 覆盖默认值
~~~

#### 5.5 强制使用位置或者关键字

> 强制使用位置或者关键字参数
>     /之前 必须为位置参数
>     *之后 必须为关键字参数
>     中间的 无所谓

~~~python
"""
    强制使用位置或者关键字参数
    /之前 必须为位置参数
    *之后 必须为关键字参数
    中间的 无所谓
"""

def func1(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)

func1(1,2,3, 4,e = 5,f = 6)
func1(1,2,3,d = 4,e = 5,f = 6)
func1(1,2,c = 3,d = 4,e = 5,f = 6)
# func1(1,2,c = 3, 4,e = 5,f = 6) 这里报错 关键字参数必须在位置参数后边

# func1(1,b = 2,c = 3,d = 4,e = 5,f = 6) # 报错 因为b必须使用位置参数
# func1(a = 1,b = 2,c = 3,d = 4,e = 5,f = 6) # 报错 因为a b 必须使用位置参数
~~~

### 6. 参数的传递

> ​	关于参数的传递 底层细节
>
> ​	在Java语言中分为值传递和引用传递 比如 10 这种数值属于值传递 而 对象这种属于引用传递
>
> ​	Python中的严格来讲 是没有值传递和引用传递的说法
>
> ​	因为在Python中所有的数据全部属于对象 都属于引用传递
> ​      在函数体内对参数的修改是否会影响原变量 完全取决于是可变类型 还是 不可变类型

~~~python
"""
    关于参数的传递 底层细节

    在Java语言中分为值传递和引用传递 比如 10 这种数值属于值传递 而 对象这种属于引用传递

    Python中的严格来讲 是没有值传递和引用传递的说法
    因为在Python中所有的数据全部属于对象 都属于引用传递
    在函数体内对参数的修改是否会影响原变量 完全取决于是可变类型 还是 不可变类型
"""

def func1(a):
    a += 1
    print("func1函数中a的取值:",a)

b = 10
func1(b)
print("实参参数b的取值:",b)

print("-----------------------------------------")

def func2(nums):
    nums[0] += 1
    print("func2函数中nums的取值为:",nums)

list1 = [1,2,3]
func2(list1)
print("list1的元素值为:",list1)

print("-----------------------------------------")

# 直接将一个列表赋值给另外一个列表 属于直接将堆内存中的地址值进行了复制

def func3(nums):
    nums[0] += 1
    print("func3函数中nums的取值为:",nums)

list1 = [1,2,3]
list2 = list1
func3(list2)
print("list1的元素值为:",list1)
print("list2的元素值为:",list2)

print("-----------------------------------------")

# 深拷贝 从外到内 都创建新的对象

import  copy
list1 = [1,2,3]

list2 = copy.deepcopy(list1)

func2(list2)
print("list1的元素值为:",list1)
print("list2的元素值为:",list2)

print("-----------------------------------------")

# 浅拷贝 外层的列表 复制全新 里边的元素 用的是同一个

list1 = [1,2,3]

list2 = list1.copy()

list3 = list1[:]

print(id(list1),id(list2),id(list3))
~~~

#### 6.1 直接赋值

![](D:\python_learning\笔记\day05-笔记\img\直接赋值.png)

~~~python
print("---------------------直接赋值 属于复制的地址值--------------------")

list1 = [1,2,3,4,5,6]

list2 = list1

print(list1)
print(list2)
print(id(list1),id(list2))
~~~

#### 6.2 浅拷贝

![](D:\python_learning\笔记\day05-笔记\img\浅拷贝.png)

~~~python
print("---------------------浅拷贝 创建新的外层对象 内层对象继续复用--------------------")

list1 = [1,2,3,[4,5,6]]

list2 = list1.copy()

print(list1,list2)
print(id(list1),id(list2))

print(list1[0] is list2[0])
print(id(list1[0]),id(list2[0]))

print(list1[1] is list2[1])
print(id(list1[1]),id(list2[1]))

print(list1[2] is list2[2])
print(id(list1[2]),id(list2[2]))

print(list1[3] is list2[3])
print(id(list1[3]),id(list2[3]))
~~~

#### 6.3 深拷贝

![](D:\python_learning\笔记\day05-笔记\img\深拷贝.png)

~~~python
print("---------------------深拷贝 从外到内 全部是新的--------------------")

import copy

list1 = [1,2,3,[4,5,6]]

list2 = copy.deepcopy(list1)

print(list1,list2)
print(id(list1),id(list2))

print(list1[0] is list2[0])
print(id(list1[0]),id(list2[0]))

print(list1[1] is list2[1])
print(id(list1[1]),id(list2[1]))

print(list1[2] is list2[2])
print(id(list1[2]),id(list2[2]))

print(list1[3] is list2[3])
print(id(list1[3]),id(list2[3]))
~~~

### 7. 返回值

> 有些函数在执行的时候，需要有返回值给调用者，通过return关键字进行返回，返回到函数调用的位置。return 用于在函数体内返回结果 返回给函数的调用者
> return表示结束函数并且返回内容

#### 7.1 为什么要使用返回值

~~~python
"""
    有些函数在执行的时候，需要有返回值给调用者，通过return关键字进行返回，返回到函数调用的位置。

    需求：编写函数计算两个函数之和 在函数之外判断最终的结果是奇数还是偶数

    return 用于在函数体内返回结果 返回给函数的调用者
    return表示结束函数并且返回内容

"""

def my_sum(a,b):
    result = a + b
    print("a与b之和为：",result)

get_data = my_sum(2,2)

print(get_data)

if 4 % 2 == 0:
    print("偶数")
else:
    print("奇数")

# 以上代码可以实现求和 但是 无法在后续的代码中利用最终的和 所以无法进行判断 相当于逻辑无法串联
# 如何让解决以上问题?使用return关键字 返回值实现


print("-----------------------------------------------------------")


def my_add(a,b):
    result = a + b
    print("a与b之和为:",result)
    return result
    print("函数继续运行") # 在Java代码中这里就报错 但是在Python中不报错 但同样永远执行不到

get_sum = my_add(24324,4)

if get_sum % 2 == 0 :
    print("偶数")
else:
    print("奇数")
~~~

#### 7.2 return的各种用法

~~~python
"""
    return关键字的其他用法
"""

def is_even(num):
    # if num % 2 == 0:
    #     return "偶数"
    # else:
    #     return "奇数"

    return "偶数" if num % 2 ==0 else "奇数"

print(is_even) # 只写函数名 属于打印函数对象 展示函数的基本信息
print(is_even(10)) # 调用函数 并且得到返回值交给print函数打印
print(is_even(11)) # 调用函数 并且得到返回值交给print函数打印


def is_even1(num):
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False
    return num % 2 == 0
print(is_even(10)) # 调用函数 并且得到返回值交给print函数打印
print(is_even(11)) # 调用函数 并且得到返回值交给print函数打印

def is_even2(num):
    # if num % 2 == 0:
    #     return 0
    # else:
    #     return 1
    return num % 2

print(is_even2(10)) # 调用函数 并且得到返回值交给print函数打印
print(is_even2(11)) # 调用函数 并且得到返回值交给print函数打印

print("-------------------------------------------------------")

def func():
    for i in range(10):
        if i == 8:
            return # 注意和break的区别
        print(i)
    print("func函数执行完毕")

func()
~~~

#### 7.3 返回多个值

~~~python
"""
    return关键字的其他用法
    return 后边返回多个值
    使用多个变量分别接收各个返回值 这个操作 也属于解包
"""

def func():
    return 1 , 2 , 3 , [4,5,6]

r1 = func() # 只写一个变量接收 所有的返回值将会自动被打包成一个元组
print(r1)

a1 , a2 , a3 , a4 = func() # 书写对与返回值相应数量的变量接收 分开处理 这种也属于解包操作
print(a1 ,a2, a3, a4)

b1 , b2 = func() # 这里报错 不允许指定不同数量的变量接收
print(b1, b2)

print("-------------------------------------------------")

def func_1(a,b,c):
    print(a,b,c)

list1 = [1,2,3]
func_1(*list1)
~~~

### 8. 多级调用

~~~python
"""
    自定义的函数之间 直接调用

    栈 stack 先进后出 后进先出 FILO
    函数执行是要进栈的 栈是一种数据结构 先进栈的 后出栈

"""

def my_func2():
    print("my_func2 开始执行")
    print("my_func2 执行完毕")

def my_func1():
    print("my_func2 开始执行**********")
    my_func2()
    print("my_func2 执行完毕**********")

my_func1()
~~~

### 9. 递归

~~~python
"""
    递归: recursive 递归和回归

    简单的理解: 函数自己调自己

    准确的理解：
    一个大的问题可以通过逻辑拆分为若干个小的问题 可以通过一个函数自己调用当前函数实现
    必须有结束的条件(递归的出口)

    举例：
    赵四  广坤  小宝  富贵  大拿



    递归的实际应用:
        求 1 ~ n之和
        求阶乘
        很多算法都会用到递归 快排 归并
        斐波那契数列
        八皇后算法
        遍历文件
        汉诺塔问题
"""

# def func1():
#     func1()
#
# func1() 这段代码 报错 因为没有结束条件

print("--------------------------求1~5之和--------------------------")

def get_num5():
    return 5 + get_num4()

def get_num4():
    return 4 + get_num3()

def get_num3():
    return 3 + get_num2()

def get_num2():
    return 2 + get_num1()

def get_num1():
    return 1

print(get_num5())

print("-------------------------求1~n之和 递归实现--------------------------")

def get_sum(num):
    if num == 1:
        return 1
    return num + get_sum(num - 1)

print(get_sum(5))

print("-------------------------求1~n之和 递归实现--------------------------")

def get_factorial(num):
    if num < 1 or num == 1:
        return 1
    return num * get_factorial(num - 1)

print(get_factorial(5))
~~~

### 10.  lambda表达式

#### 10.1 介绍

> lambda 匿名函数 面向函数编程 不关注谁来做 只关注做什么

~~~python
"""
    lambda 匿名函数 面向函数编程 不关注谁来做 只关注做什么
    ctrl + alt + L 自动格式化对齐代码
"""

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def operation(a,b,func):
    return func(a,b)

print(add)
print(sub)
print(mul)
print(div)

print(operation(1, 2, mul))

print("*" * 50)

operation(1,2,lambda a ,b : a + b)

print(lambda a ,b : a + b)
print(type(lambda a ,b : a + b))
~~~

#### 10.2 常用函数

~~~python
"""
    lambada主要作用 用于处理数据的 是一种语法简洁的优化方式
    使用lambda处理数据
"""
from functools import reduce

# list1 = [2,1,4,6,3]
# list1.sort(reverse=True)
# print(list1)
# print(sorted(list1,reverse=True)) 排序操作 reverse = True 表示降序


person_list = [
    {"name": "jack", "age": 21, "address": "深圳"},
    {"name": "jeery", "age": 11, "address": "深圳"},
    {"name": "tom", "age":35, "address": "广州"},
    {"name": "john", "age": 25, "address": "广州"},
    {"name": "Lily", "age": 55, "address": "北京"},
]

print("---------------------------sorted函数 排序---------------------------------")
# 按照年龄升序或者降序排序 reverse=True 表示降序
print(sorted(person_list,key=lambda p : p["age"],reverse=True))

print(sorted(person_list,key=lambda p : p["name"],reverse=True))

print("---------------------------map函数 映射---------------------------------")
# 呈现每个人姓名的大写形式

print(list(map(lambda p: p["name"].upper(), person_list)))

print("---------------------------filter函数 过滤---------------------------------")
# 查找地址为深圳的人
print(list(filter(lambda p: p["address"] == "深圳", person_list)))

# 查找未成年的人
print(list(filter(lambda p: p["age"] < 18, person_list)))

print("---------------------------reduce函数 合并操作---------------------------------")

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))

# 统计列表中所有人的年龄综合
# print(reduce(lambda p1, p2: p1["age"] + p2["age"], person_list)) # 这里报错 因为年龄相加之后 无法直接赋值给某个字典对象

person_list = [
    {"name": "jack", "age": 21, "address": "深圳"},
    {"name": "jeery", "age": 11, "address": "深圳"},
    {"name": "tom", "age":35, "address": "广州"},
    {"name": "john", "age": 25, "address": "广州"},
    {"name": "Lily", "age": 55, "address": "北京"},
]

print(reduce(lambda p1, total_age: p1["age"] + total_age, person_list))


~~~

### 10. 函数的注释(了解)

~~~python
"""
    多行注释 本质为实现字符串
"""


def dog (name:str, age:(1, 99),species:'狗狗的品种') -> tuple:
    """
    这个函数用于讲解函数的注释
    :param name:这是名字参数
    :param age:这是年龄参数
    :param species:品种参数
    :return:返回值
    """
    print(name , age , species)
    return True

dog(123,"abc",True)

print(dog.__annotations__)

help(dog)
~~~







