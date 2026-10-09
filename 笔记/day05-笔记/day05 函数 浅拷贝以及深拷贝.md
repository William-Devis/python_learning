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







