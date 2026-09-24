## day04 容器和函数

### 1. list列表

#### 1.1 列表基础操作

~~~python
"""
    列表操作
"""

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d"]
print(list1 + list2) # 内容拼接到一起

print(list1 * 2) # 每个元素复制一份

print(list2 * 3) # 每个元素复制对应的份数

print("------------------------------------------")

list1 = [1, 2, 3, 4, 5]

list1[0] = 100 # 直接指定下标修改元素

print(list1)

print("------------------------------------------")

list1 = [1, 2, 3, 4, 5]

list1[1:3] = [666] # 将指定范围的数据改为单个数据 注意：必须用中括号包括

print(list1)

print("------------------------------------------")

list1 = [1, 2, 3, 4, 5]

list1[1:3] = [11,22,44,66,78] # 将指定范围的数据改为多个数据

print(list1)

print("------------------------------------------")

list1 = [1, 2, 3, 4, 5]

list1[1:3] = ["a","b","hello world"] # 将指定范围的数据改为多个数据 可以是不同的类型

print(list1)
~~~

#### 1.2 常用函数

~~~python
"""
    列表操作
"""
print("--------------------获取列表长度---------------------")

list1 = [1, 2, 3, 4, 5]

print("元素的个数",len(list1))

print("--------------------获取列表最大、最小值---------------------")

list1 = [111, 2, 3, 4, 5]

print(max(list1))

print(min(list1))

print("--------------------获取列表元素之和---------------------")

list1 = [111, 2, 3, 4, 5]

print(sum(list1)) # 注意元素只能为数值类型的

# list2 = ["a", "b", "c", "d"]

# print(sum(list2))
~~~



#### 1.3 列表的遍历

~~~python
"""
    列表的遍历操作
"""
print("-----------------------列表的遍历操作----------------------")

list1 = [11, 22, 33, 44, 55]

for i in list1:
    print(i)

print("-----------------------列表的遍历操作----------------------")

for i in range(len(list1)):
    print(i,list1[i])

print("-----------------------列表的遍历操作 使用enumerate函数 ----------------------")

for i , value in enumerate(list1):
    print(i,value)

print("-----------------------列表的遍历操作 使用enumerate函数 指定start参数----------------------")

for i , value in enumerate(list1,start=1): # 可以指定起始的标记数值 依然是从0下标开始遍历 只是数值改变了
    print(i,value)
~~~



#### 1.4 列表删除，推导式和常用操作

~~~python
"""
    列表操作
"""

print("----------------列表的删除操作----------------")

list1 = [11, 22, 33, 44, 55]

del list1[0] # 直接删除指定的下标元素

print(list1)

print("----------------嵌套列表的操作----------------")

list12 = [[1, 2, 3],['a','b','c'],[True,False,True]]

for item in list12:
    # print(item) # 直接输出 属于打印外层列表中的每一个小(子)列表
    for value in item: # 嵌套循环 继续迭代内层的列表
        print(value,end="\t")
    print()

print("----------------列表推导式----------------")

# 通过表达式的方式 快速创建一个列表

list1 = [i for i in range(1,11)] # i的取值从1~10 存放在列表中

print(list1)

list2 = [x**2 for x in range(5)] # i的取值从1~10 再**2 存放在列表中

print(list2)

list3 = [x**2 for x in range(5) if x % 2 ==0] # i的取值从0~4 只筛选偶数 再**2 存放在列表中

print(list3)

list1 = [11, 22, 33, 44, 55]

list2 = list1[:]

print(list2)

list3 = [x for x in list1] # 通过列表推导式的方式复制一个列表

print(list3)

list4 = ['a','b','c']

list5 = [1,2,3]

list6 = [(i,j) for i in list4 for j in list5]

print(list6)

print("----------------列表Zip函数----------------")

# 将两个列表打包在一起

list4 = ['a','b','c']

list5 = [1, 2, 3, 4]

zipped = zip(list4,list5) # 如果两个列表长度不一致 以长度短的为主

print(zipped)

list6 = list(zipped)

print(list6)

print("----------------列表list函数 转换列表----------------")

list_1 = list("abcdef")

print(list_1)

list_1 = list("123456")

print(list_1)

list_1 = list((1,2,3,4,5)) # 传入元组类型

print(list_1)
~~~



#### 1.5 列表排序

~~~python
"""
    列表操作
"""

print("----------------列表的添加操作----------------")

list1 = [11, 22, 33, 44, 55]

list1.append(666)

print(list1)

list1.append([333, 444, 555]) # 添加的是一个列表 依然作为一个元素处理

print(list1)

list1.extend([5,7,9,0]) # 扁平化处理

print(list1)

print("----------------列表的添加操作----------------")

list2 = [11, 2, 24, 4, 55]

# 默认升序 修改原列表 没有返回值 如果要接收 只能得到一个None
# 因为Python中 没有返回值的函数 返回值为None
list.sort(list2) # 原地修改

print(list2)

list2 = [11, 2, 24, 4, 55]

list.sort(list2,reverse=True) # 这种操作属于降序操作

print(list2)
~~~

### 2. str字符串

> str 字符串的使用
>     字符串是不可变的、有序的
>     字符串中的元素不可修改
>     字符串使用单引号、双引号或三重引号定义
>     字符串中每个值都有对应的位置值，成为索引或下标，索引从起始从0开始向后逐个递，并且从末尾从-1开始逐个向前递减

#### 2.1 基础操作

~~~python
"""
    str 字符串的使用
    字符串是不可变的、有序的
    字符串中的元素不可修改
    字符串使用单引号、双引号或三重引号定义
    字符串中每个值都有对应的位置值，成为索引或下标，索引从起始从0开始向后逐个递，并且从末尾从-1开始逐个向前递减
"""

print("------------------字符串的访问-------------------")

s1 ="hello world"

print(s1)
print(s1[0])
print(s1[-1])
print(s1[1:3])
print(s1[4:-3])

print("------------------字符串的加法-------------------")

s1 ="hello world"
s2 ="hello world"

print(s1 + s2)

print("------------------字符串的乘法-------------------")

print(s2 * 2)

print("------------------字符串的成员运算符-------------------")

print("h" in s2)
print("x" in s2)

print("------------------原始字符串-------------------")
# 在字符串前 加上R或者r 都可以保留原始的字符串
s1 = r"hello \n world"
print(s1)

s1 = R"hello \n world"
print(s1)
~~~

#### 2.2 常用函数

~~~python
"""
    str 字符串的常用函数
    字符串是不可变的、有序的
    字符串中的元素不可修改
    字符串使用单引号、双引号或三重引号定义
    字符串中每个值都有对应的位置值，成为索引或下标，索引从起始从0开始向后逐个递，并且从末尾从-1开始逐个向前递减
"""

print("------------------replace函数------------------")

s1 = "abc abc abc"

s2 = s1.replace("abc","def")

print(s2)

print(s1)

print("------------------replace函数 指定替换数量------------------")

s1 = "abc abc abc"

s2 = s1.replace("abc","世界你好",2)

print(s2)

print("------------------split函数------------------")

s1 = "abc abc abc"

print(s1.split(' ')) # 拆分字符串

s1 = "abc-abc-abc"

print(s1.split('-'))

s1 = "abc-abc-abc"

print(s1.split('*'))

print("------------------join函数------------------")
# 指定符号 拼接字符串
list_str = ["https://www","atguigu","com"]

print(".".join(list_str))

print("------------------strip函数------------------")

# 去除字符串两边的空格 或者指定字符

s1 = "   a \t \t b \t \t  c   "

print(s1.strip())
print(len(s1.strip()))

print(s1.replace(" ", "")) # 这里是将空格字符 替换为了没有空格 但是只能替换空格

print("------------------删除前缀removeprefix------------------")

s1 = "abc hello world xyz"

print(s1.removeprefix("xyz"))

print("------------------upper函数 转换为大写-----------------")

s1 = "abc hello world xyz"

s2 = s1.upper()

print(s2)

print("------------------lower函数 转换为小写-----------------")

s2 = s1.lower()

print(s2)

print("------------------swapcase函数 翻转大小写-----------------")

s1 = "AbCdEf"

print(s1.swapcase())

print("------------------capitalize函数 第一个字母变大写 其他变小写-----------------")

s1 = "aBCEDF"

print(s1.capitalize())

print("------------------title函数 将单词转换为标题格式-----------------")
# 每个单词首字母大写

s1 = "student_name"

print(s1.title())

print("------------------max、min函数 转换为大、小写-----------------")

s1 ="abcABC中"

print(max(s1))
print(min(s1))

print("------------------find函数 查找字符串-----------------")

# 查找字符串第一次出现的位置 返回值为下标

print(s1.find("a"))
print(s1.find("ab"))
print(s1.find("abc"))
print(s1.find("xyz")) # 如果找不到 则返回-1
print(s1.find("hello world")) # 如果找不到 则返回-1

print("------------------index函数 查找字符串-----------------")

s1 = "abc abc abc"

print(s1.index("a"))
print(s1.index("ab"))
print(s1.index("abc"))
# print(s1.index("xyz")) # 找不到则报错

print("------------------count函数 统计字符串-----------------")

print(s1.count("a"))
print(s1.count("ab"))
print(s1.count("abc"))
print(s1.count(" "))
print(s1.count("xyz"))

print("------------------startswith函数 判断是否已指定的内容开头----------------")

s1 = "abc abc abc"

print(s1.startswith("a"))
print(s1.startswith("ab"))
print(s1.startswith("abc"))
print(s1.startswith("abc "))
print(s1.startswith("xyz"))

print("------------------endswith函数 查找字符串-----------------")

s1 = "abc abc abc"

print(s1.endswith("c"))
print(s1.endswith("bc"))
print(s1.endswith("abc"))
print(s1.endswith("xyz"))

print("------------------isspace函数 判断字符串是否全部为不可见字符-----------------")

s1 = "    "

print(s1.isspace())

s1 = "   \n   \t   "

print(s1.isspace())
~~~

#### 2.3 其他函数

~~~python
"""
    字符串其他函数
"""

print("-----------------center函数 居中效果-----------------")

s1 = "abc abc"
print(s1.center(20))
print(s1.center(20,"*"))

print("------------------isalnum函数 判断内容-----------------")

# str.isalnum() 检查字符串是否非空且只包含字母(英文字母+汉字)和数字

s1 = "abc中1"
print(s1.isalnum())

s2 = "abc_中*1"
print(s2.isalnum())

print("------------------isalpha函数 判断内容-----------------")

# str.isalpha() 检查字符串是否非空且只包含字母(英文字母+汉字)

s1 = "abc中1"
print(s1.isalpha())

s2 = "abc中"
print(s2.isalpha())

print("------------------isascii函数 判断内容-----------------")

# str.isalpha() 检查字符串是否非空且只包含字母(英文字母+汉字)

s1 = "abc ABC"
print(s1.isascii())

s2 = "abc ABC 中文"
print(s2.isascii())

s3 = "abc ABC 123"
print(s3.isascii())

print("------------------isdecimal函数 判断内容-----------------")

s1 = "1 2 3 4"
print(s1.isdecimal())

s2 = "1234"
print(s2.isdecimal())

s3 = "0B1111"
print(s3.isdecimal())

print("------------------isdigit函数 判断内容-----------------")
# isdigit() 检查字符串是否非空且只包含数字

s1 = "123²³"
print(s1.isdigit())
~~~

### 3. 元组tuple

#### 3.1 元组的创建

> 元组的创建
>     元组是一个不可变的、有序的元素集合。
>     不能对元组中的元素进行修改操作。
>     元组使用 () 定义，数据之间使用，分隔。
>     元组中每个元素都有对应的位置值，称为索引或下标，索引从起始从0开始向后逐个递增，并且末尾从-1开始逐个向前递减。
>     元组中元素可以是不同的类型。
>     元组的使用方式与列表类似

~~~python
"""
    元组的创建
    元组是一个不可变的、有序的元素集合。
    不能对元组中的元素进行修改操作。
    元组使用 () 定义，数据之间使用，分隔。
    元组中每个元素都有对应的位置值，称为索引或下标，索引从起始从0开始向后逐个递增，并且末尾从-1开始逐个向前递减。
    元组中元素可以是不同的类型。
    元组的使用方式与列表类似
"""

print("*****************元组的创建***************")
tuple1 = (1,22,33,4,55,6,)
print(tuple1)
print(type(tuple1))

tuple2 = (1,) # 如果只有一个元素 必须加上逗号
print(tuple2)
print(type(tuple2))

print("*****************元组的创建 元组推导式***************")
list1 = [x for x in range(1,11)]
print(list1)
gen_obj = (x for x in range(1,11) if x % 2 == 0) # 这里返回值为生成器对象
print(gen_obj)
tuple3 = tuple(gen_obj) # 结合tuple函数 创建tuple对象
print(tuple3)
~~~

#### 3.2  元组的使用

> 元组的使用
>     元组是一个不可变的、有序的元素集合。
>     不能对元组中的元素进行修改操作。
>     元组使用 () 定义，数据之间使用，分隔。
>     元组中每个元素都有对应的位置值，称为索引或下标，索引从起始从0开始向后逐个递增，并且末尾从-1开始逐个向前递减。
>     元组中元素可以是不同的类型。
>     元组的使用方式与列表类似

~~~ python
"""
    元组的使用
    元组是一个不可变的、有序的元素集合。
    不能对元组中的元素进行修改操作。
    元组使用 () 定义，数据之间使用，分隔。
    元组中每个元素都有对应的位置值，称为索引或下标，索引从起始从0开始向后逐个递增，并且末尾从-1开始逐个向前递减。
    元组中元素可以是不同的类型。
    元组的使用方式与列表类似
"""

print("*****************元组的使用 方式基本与list一致***************")
tuple1 = (1,22,33,4,55,6,)

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])
print(tuple1[5])

# print(tuple1[6]) 超出下标范围报错

print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])
print(tuple1[-4])
print(tuple1[-5])
print(tuple1[-6])

print("*****************元组的切片 方式基本与list一致***************")

print(tuple1[0:3])
print(tuple1[0:-2])
~~~

#### 3.3 元组计算

~~~python
"""
    元组的计算
"""
print("*****************元组的计算 规则基本与list一致***************")
tuple1 = (1,2,3,)
print(tuple1)

tuple2 = ('a', 'b', 'c')
print(tuple2)
print(tuple1 + tuple2)

print(tuple1 * 2)
print(tuple2 * 2)

# print(tuple1 - tuple2) 不能减法
# print(tuple1 / tuple2) 不能除法
~~~

### 3.4 基本使用

~~~python
"""
    tuple基本使用
"""

print("-------------成员运算符的使用--------------")
tuple1 = (1,22,33,4,55,6,)

print(1 in tuple1)
print(2 in tuple1)

print("-------------len函数获取元组中的元素个数--------------")
tuple1 = (1,22,33,4,55,6,)

print(len(tuple1))

print("-------------max min sum 函数用法一致--------------")
tuple1 = (1,22,33,4,55,6,)

print(max(tuple1))
print(min(tuple1))
print(sum(tuple1))

tuple2 = ('a', 'b', 'c', 'd', 'e', '你')
print(max(tuple2))
print(min(tuple2))
# print(sum(tuple2)) 对于元素类型为字符串类型 可以找最大最小值 但是不能求和
~~~

#### 3.5 元组的遍历

~~~python
"""
    元组的遍历
"""

print("-------------元组遍历--------------")

tuple1 = (1,22,33,4,55,6,)

for i in tuple1:
    print(i)

print("-------------len函数遍历--------------")

for i in range(len(tuple1)):
    print(i,tuple1[i])

print("-------------enumerate遍历--------------")

for i ,v in enumerate (tuple1,start=1): # 指定start 表示序号从1开始 注意 还是从下标为0的元素遍历的
    print(i,v)
~~~

#### 3.6 元组的不可变性

![](D:\尚硅谷AI开发\笔记\day04-笔记\img\元组的不可变性.png)

~~~ python
"""
    元组不可变
    元组不可变 表示元组在内存中的地址是无法改变
    至于元组中的元素是否可以改变 要根据元素具体的类型决定

    Python中也是存在GC Garbage Collection 机制的 解释器会自动回收无需继续存在的对象
    没有任何引用指向此对象 那么此对象将会被回收
"""

t1 = (1,22,33,4,55,6,)

print(t1[0])

# tuple1[0] = 100 元组中的元素不支持重新赋值

print(t1)

t1 = t1 + (11, 22, 33)
print(t1)
print(id(t1))

t2 = (1,2,3,[33,44,55])

print(t2[3])

t2[3].append(66) # 这里单独修改列表中的值 不影响元组的地址

print(t2)
print(id(t2))
~~~

### 4.集合

#### 4.1集合的创建

> 集合的创建方式
>     集合是无序的，且不包含重复的元素。
>     集合使用 {} 定义，数据之间使用 ，分隔，也可以使用set()定义。
>     集合没有索引，所以不能通过切片的方式访问集合元素。
>     集合中元素可以是不同的类型。
>     集合可以进行数学上的集合操作，如并集、交集和差集。
>     集合适用于需要快速成员检查、消除重复项和集合运算的场景。

~~~python
"""
    集合的创建方式
    集合是无序的，且不包含重复的元素。
    集合使用 {} 定义，数据之间使用 ，分隔，也可以使用set()定义。
    集合没有索引，所以不能通过切片的方式访问集合元素。
    集合中元素可以是不同的类型。
    集合可以进行数学上的集合操作，如并集、交集和差集。
    集合适用于需要快速成员检查、消除重复项和集合运算的场景。
"""

set1 = {1,2,3,4,5,6}
print(set1)
print(type(set1))

set2 = set([1,2,3,4,5,6])
print(set2)
print(type(set2))

set3 = set()
print(set3)
print(type(set3))

set4 = {}
print(set4)
print(type(set4)) # 这种是字典 注意

set5 = {x for x in range(5)}
print(set5)
print(type(set5))
~~~

#### 4.2 集合的常用操作

~~~python
"""
    集合的常用操作
"""

print("-----------------set添加操作----------------")

set1 = {1,2.3,4,5,6}

set1.add(7) # 添加元素之前 是会检查是否有重复项 有则不添加

print(set1)

set1.add(5)

print(set1)

print("-----------------set删除操作----------------")

set1 = {1,2.3,4,5,6}

set1.remove(4)

print(set1)

print("-----------------set成员运算符操作----------------")

print(1 in set1)
print(2 in set1)
print(8 in set1)

print("-----------------set len函数----------------")

set1 = {1,2,3,4,5,6}

print(len(set1))

print("-----------------max min sum操作----------------")

set1 = {1,2,3,4,5,6}
print(max(set1))
print(min(set1))
print(sum(set1))

set2 = {"a","b","c","d","e","f"}
print(set2)
print(max(set2))
print(min(set2))
# print(sum(set2)) 无法求和计算

~~~

#### 4.3 集合的其他操作

~~~python
"""
    set其他操作
"""

print("-------------------set遍历操作----------------")

set1 = {1,2,3,4,5,6}

for i in set1:
    print(i)

print("-------------------set遍历操作----------------")
# update函数依然属于添加操作 对比add 支持更多的类型 比如容器类型

set1 = {1,2,3,4,5,6}

set1.add(8)

set1.update({22,44,55,66})

print(set1)

print("-------------------set union操作----------------")

set1 = {1,2,3,4,5,6}

set2 = set1.union({11,22,33}) # 返回新的集合 所以需要接收 原集合不变

print(set1)

print(set2)

print("-------------------remove操作----------------")

set1 = {1,2,3,4,5,6}

set1.remove(1)

print(set1)

# set1.remove(7) # 删除不存在的 会报错

print(set1)

print("-------------------set discard操作----------------")

set1 = {1,2,3,4,5,6}

set1.discard(2)

print(set1)

set1.discard(8) # 这里删除不存在的 不会报错

print(set1)
~~~

#### 4.4 集合常用函数

~~~python
"""
    集合常用函数
"""

print("-----------------pop函数 随机取数据----------------")

set1 = {1,2,3,4,5,6}

print(set1.pop())

set2 = {"abc","hello","text", "a","b","c"}

print(set2.pop())

set3 = set()

# print(set3.pop()) # 集合为空 不能使用pop，会报错

print("-----------------clear函数 清空集合----------------")

set1 = {1,2,3,4,5,6}

set1.clear()

print(set1)

print("-----------------求差集 difference----------------")

# difference 执行完以后会得到一个新的集合
set1 = {1,2,3,4}
set2 = {3,4,5,6}

diff_set1 = set1.difference(set2)

print(diff_set1)

diff_set2 = set2.difference(set1)

print(diff_set2)

print(set1)
print(set2)

print("-----------------求差集 difference_update----------------")
# 原地修改

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set1.difference_update(set2)

print(set1)
print(set2)

print("*" * 20)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set2.difference_update(set1)
print(set1)
print(set2)

print("-----------------求交集 intersection----------------")

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1.intersection(set2)
print("set3:",set3)

print(set1)
print(set2)
print("*" * 20)

set4 = set2.intersection(set1)
print("set4:",set4)
print(set1)
print(set2)

print("-----------------求交集 &----------------")

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1 & set2
print("set3:",set3)

print("-----------------求交集 |----------------")

set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1 | set2
print("set3:",set3)

print("-----------------求差集 - ----------------")
set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1 - set2
print("set3:",set3)

set4 = set2 - set1
print("set4:",set4)

# print(set1 + set2) 不能加 否则报错
# print(set1 / set2) 不能除 否则报错

print("-----------------isdisjoint 判断是否没有交集 - ----------------")

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.isdisjoint(set2))

print("-----------------issubset 判断是否是子集 -----------------")

set1 = {3,4}
set2 = {3,4,5,6}

print(set2.issubset(set1))

print("-----------------copy 拷贝集合 -----------------")

set2 = {3,4,5,6}

set3 = set2.copy()

print("set3:",set3)
~~~

### 5. dict字典

#### 5.1 创建字典

> 一个无序的键值对集合，键是唯一的，而值可以重复。
>     字典使用 {} 定义，键 (key) 和值 (value) 使用 ：连接，每个键值对之间使用，分隔。如{key1 : value1, key2 : value2}
>     字典没有索引。
>     字典可以通过键来获取对应的值。
>     值可以取任何数据包类型，但键必须是不变的，如字符串、数字、元组

~~~ python
"""
    一个无序的键值对集合，键是唯一的，而值可以重复。
    字典使用 {} 定义，键 (key) 和值 (value) 使用 ：连接，每个键值对之间使用，分隔。如{key1 : value1, key2 : value2}
    字典没有索引。
    字典可以通过键来获取对应的值。
    值可以取任何数据包类型，但键必须是不变的，如字符串、数字、元组
"""
print("-------------------------字典的创建---------------------")
dict1 = {}

print(dict1)

dict2 = dict()

print(dict2)

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print(dict3)

dict4 = dict(name = "赵四" , age = 18 , gender = "male")

print(dict4)

dict5 = dict([("name","赵四"),("age","18"),("gender","male")])

print(dict5)

squares = {x: x**2 for x in range(4)} # 通过字典推导式
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9}
~~~

#### 5.2 字典的访问

~~~python
"""
    字典的使用
"""

print("---------------------字典的访问----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print(dict3["name"])
print(dict3["age"])
# print(dict3["address"]) # 如果键不存在 会报错

print("---------------------字典的访问 通过 get 函数访问----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male","name" : "小宝"}

print(dict3.get("name"))
print(dict3.get("age"))
print(dict3.get("gender"))
print(dict3.get("address"))
print(dict3.get("address","深圳")) # 如果为None 指定默认值为 “深圳”

print("---------------------字典的访问 添加数据----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male", "name" : "小宝"}

dict3["city"] = "深圳"

print(dict3)

print("---------------------字典的访问 修改数据----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

dict3["name"] = "小宝"

print(dict3)

print("---------------------字典的访问 查看是否包含某个键----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print("name" in dict3)
print("赵四" in dict3)

print("---------------------字典的访问 len函数----------------")

dict3 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print(len(dict3))
~~~

#### 5.3 字典的遍历

~~~python
"""
    字典的遍历
    keys() 函数获取所有的键 然后再根据键获取值
    values() 函数获取所有的值
    items() 获取所有的键值对
"""
from day04.demo1.test_list_3 import value

print("---------------------字典的遍历 keys函数----------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

keys = dict1.keys()

print(keys)
print(type(keys))

# 遍历键的容器
for key in keys:
    # 根据键获取值
    print(key,dict1[key],dict1.get(key))

print("---------------------字典的遍历 values函数----------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

values = dict1.values()

print(values)
print(type(values))

for value in values:
    print(value)

print("---------------------字典的遍历 items函数----------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

items = dict1.items()
for key, value in items:
    print(key,value)
~~~

#### 5.4 字典的删除和常用函数

~~~python
"""
    字典的删除和常用函数
"""

print("-------------------------删除元素---------------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

del dict1 ["name"]
print(dict1)

print("-------------------------pop函数---------------------")

# 获取元素 并且删除
dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print(dict1.pop("name"))

print(dict1)

print("-------------------------clear函数---------------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

dict1.clear()

print(dict1)

print("-------------------------update函数---------------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

dict2 = {"a" : "A" , "b" : "B" ,"c" : "C"}

dict1.update(dict2) # 更新内容到dict1中去

print(dict1)
print(dict2)

print("-------------------------setdefault函数---------------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

print(dict1.setdefault("name")) # 如果存在 则直接获取
dict1.setdefault("city","深圳") # 如果不存在 则添加并且获取
print(dict1)

print("-------------------------copy函数---------------------")

dict1 = {"name" : "赵四" , "age" : 18 , "gender" : "male"}

dict2 = dict1.copy()

print(dict2)
~~~

#### 5.5 四种容器对比

![](D:\尚硅谷AI开发\笔记\day04-笔记\img\容器的对比.png)



