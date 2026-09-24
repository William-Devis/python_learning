## day02 变量数据类型 & 输入输出

### 1. python语言的执行

![](D:\尚硅谷AI开发\笔记\day02-笔记\img\python语言执行过程.png)

### 2.小整数池

![](D:\尚硅谷AI开发\笔记\day02-笔记\img\小整数池.png)

~~~python
"""
    小整数池    CPython解释器将-5 ~ 256 这个范围的整数 存在小整数池    当我们声明变量
    取值属于这个范围的数据    将直接使用小整数池中的对象   不会重复创建多个对象
    这样设计的目的   是为了节省内存资源

    在终端通过交互式的方式可以直接感受上方的描述 如果在Pycharm中 因为Pycharm对整数的存储也做了优化
    所以不需要记忆 按照CPython解释器的规则来记忆即可
    Java语言也有这样的设计   将Byte有符号取值范围(-128 ~ 127)内的数据 存放在一个 缓存数组中 CacheArray

    因为不可变 才可以共享
"""

a = 10
b = 10
c = 10
print(a)
print(b)
print(c)

# 呈现内存中的地址值
print(id(a))
print(id(b))
print(id(c))

# 通过is关键字 比较是否属于同一个对象 注意：严格比较内存地址
print(a is b)
print(a is c)
print(b is c)

print("--------------------------")

a = 300
b = 300
c = 300
print(id(a))
print(id(c))
print(id(b))

print(a is b)
print(b is c)
print(a is c)

# 以上代码在终端中执行 观察效果
~~~

### 3.float类型

> float类型属于浮点数类型 小数类型 是有精度损失的 任何语言 只要采用的是IEEE754的这个标准定义的类型都有这个问题 因为CPU采用这个标准 所以计算机语言使用相同的标准 运算效率更高 但是精度无法保证 如果需要保存货币 进行科学计算 等对精度有要求的情况下 可以使用Decimal类 此类使用字符转的方式来记录任何精度 任何大小的数据 并且数据是准确的 不存在任何误差

~~~python
a = 0.1
b = 0.2
print(a + b) # 0.30000000000000004 精度缺失
print(type(a))
print(type(b))

# 从名为decimal的模块中导入了Decimal这个类
from decimal import Decimal
a = Decimal("0.3432524254535")
b = Decimal("0.6757456645646")
print(type(a))
print(type(b))
print(a + b)
print(a * b)
print(a / b)
~~~

### 4.bool类型

![](D:\尚硅谷AI开发\笔记\day02-笔记\img\bool类型.png)

> 因为C语言中是没有布尔类型的 使用1或者0来表示真或者假
>
> 而Python延续了这个规则Python中的bool 类型 True 也可理解为1   False理解为0
>
> True 以及 False 被Python设计为全局单个对象 Global Single Object
>
> 即整个Python进程中 所有的True都是一个对象  所有的False也是一个对象
>
> ==比较值 值相同 地址值未必相同
>
> is比较地址值 地址值相同 值一定相同

~~~py
a = True
b = True
print(a)
print(b)
print(type(a))
print(type(b))

# == 用于比较左右两边值是否相同
print(a == 1)
print(b == 0)
print(a + 1)

# is 严格比较地址 即判断内存中是否属于同一个对象
print(a is 1)
print(b is 0)

print("*" * 100)

b1 = True
b2 = True
b3 = True
print(b1 == b2) # 比较值
print(b1 is b2) # 比较内存中的地址
print(b1 is b3) # 比较内存中的地址
print(b2 is b3) # 比较内存中的地址

print("*" * 100)
b1 = False
b2 = False
b3 = False
print(b1 == b2) # 比较值
print(b1 is b2) # 比较内存中的地址
print(b1 is b3) # 比较内存中的地址
print(b2 is b3) # 比较内存中的地址
~~~

> 在开发中 一些特殊的值或者空容器 也可以表示为False
> None 0 0.0 "" [] () {}
> None也被设计为全局单例对象 即同一个Python进程中 所有的None对象都是同 
>
> 一个 也是为了节省内存资源

~~~py
if not None:
    print("条件成立1")

if not 0:
    print("条件成立2")

if not 0.0:
    print("条件成立3")

if not []:
    print("条件成立4")

if not ():
    print("条件成立5")

if not {}:
    print("条件成立6")

a = None
print(a == False)
print(a is False)

b = None
c = None
d = None
print(a == b)
print(a == c)
print(a == d)
print(a is b)
print(a is c)
print(a is d)

print("程序结束")
~~~

### 5.str类型

> str类型 字符串类型
> 任何被英文双引号或者单引号包括的内容 都属于字符串的实例 也就是对象
>
> Literal 字面量 对于字符串而言 直接书写在双引号或者单引号之内 这个值属于字面量 属于与字面量
> 字面量都属于常量 常量不能修改

~~~py
s1 = "abc"
s2 = "ABC"
s3 = "hello world"

print(s1)
print(s2)
print(s3)
print(s1 + s2 + s3) # 字符串的加法计算属于拼接字符串

print(type(s1))
print(type(s2))
print(type(s3))


html_str = "<html>\
       <head>\
          <title>这是我的第一个网页</title>\
       </head>\
       <body>\
       网页的内容......\
       </body>\
</html>"

html_str2 = """<html>
       <head>
          <title>这是我的第一个网页</title>
       </head>
       <body>
            网页的内容......
       </body>
</html>"""
~~~

### 6.转义字符

> 我们使用转义字符来保存一个特殊符号 或者 实现一些特定的效果

~~~python
s1 = "\\\\"
print(s1)

s2 = "\""
print(s2)

s3 = "'"
print(s3)

s4 = "\'"
print(s4)

s5 = '\''
print(s5)

s6 = "abc\bdef" # 退格
print(s6)

s7 = "a\nb\nc" # 换行
print(s7)

# 制表符
s8 = "床\t\t前\t明\t月\t光"
s9 = "疑\t\t是\t地\t上\t霜"
print(s8)
print(s9)

# 注意 \r 只是回车的效果 即回到行首
s10 = "abc\rdef"
print(s10)
~~~

### 7.str类型的intern机制

> str类型的intern机制
>     为了共享str对象 节省内存资源 str类型的对象默认是开启intern机制的
>     除非字符串中包含一些特殊的符号 或者 空格等

~~~python
s1 = "abc"
s2 = "abc"
print(s1)
print(s2)
print(s1 == s2)
print(s1 is s2)
print(id(s1))
print(id(s2))

s3 = "a b c"
s4 = "a b c"
print(s3 == s4)
print(s3 is s4)
print(id(s3))
print(id(s4))
~~~

![](D:\尚硅谷AI开发\笔记\day02-笔记\img\str类型的intern机制.png)

### 8.类型转换

### 8.1自动类型转换

> 自动类型转换 我们在使用不同的类型数据进行计算 会涉及到自动类型转换
> 对于整数和浮点数进行计算 结果会自动转换为浮点数类型

~~~python
a = 10
b = 2.5
result1 = a + b
print(result1)
print(type(result1))

c = 10
d = 1
result2 = c / d
print(result2)
print(type(result2))


# 跟Java语言不同 Python中不允许数值和字符直接加法计算
e = 10
f = "hello"
# 错误(异常)会导致程序中断 后续我们可以通过异常处理机制 来捕获异常
print(e + f) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("程序结束")
~~~



### 8.2强制类型转换

##### int函数

~~~python
"""
    强制类型转换
"""

# int 函数 将带入的内容转换为整数 小数部分舍弃

print(int(2.5))

num1 = int(2.5)
print(num1)

# 3E5 属于科学计数法 3 * 10 ^ 5
num2 = 3.3E10
print(num2)
# 将传入的科学计数法 转换为int类型
print(int(3.3E2))

print("*" * 50)

# 字符串类型转换为int类型
s1 = "10"
a1 = int(s1)
print(type(a1))
print(a1)

print("*" * 50)

s1 = "-10"
a1 = int(s1)
print(type(a1))
print(a1)

print("*" * 50)

s1 = "   -10   "
a1 = int(s1)
print(type(a1))
print(a1)

print("*" * 50)

print(int("111"))
print(int("111",2))
# 使用八制来处理字符串数据
print(int("11",8))
# 使用十六进制来处理字符串数据
print(int("11",16))
print(int("4e2d",16))
# print(int("4e2d",2)) 这里报错 ValueError: invalid literal for int() with base 2: '4e2d'

# 使用二进制来处理字符串数据
print(int("0B1111",2))
# 让Python解释器自行按照合适的进制处理
print(int("0B1111",0))
# print(int("0B1111")) 对于不能直接处理为十进制数值的字符串 必须指定要处理的进制 否则报错

print(int("0o11",8))
print(int("0o11",0))
# print(int("0o11")) 对于不能直接处理为十进制数值的字符串 必须指定要处理的进制 否则报错

print(int("0X4E00",16)) # 中文汉字一
print(int("0X9FA5",16)) # 中文汉字龥
~~~

##### float函数

~~~python
"""
    强制类型转换 float函数
    将传入的数据转换为浮点数
"""

s1 = "11.5"
f1 = float(s1)
print(f1)
print(type(f1))

print("*" * 50)

print(float("3E5"))

print("*" * 50)

# nan 或者 Nan : not a number 不是一个数值

print(float("nan"))
print(float("NaN"))

# inf 或者 infinity
print(float("inf"))
print(float("infinity"))

# print(float("abc")) 报错 并非支持所有字符串
~~~

##### complex函数

> 复数函数 complex()
>
> 数学中使用i表示虚部 Python中使用1j表示
>
> 因为在电气工程学领域i表示电流符号 所以在Python特意避免歧义 避免混淆

~~~python
c1 = complex(1,2)
print(c1)
print(c1.real)
print(c1.imag)


c2 = complex("1+2j")
print(c2)
print(c2.real)
print(c2.imag)
~~~

##### str函数

> str函数 将传入的数据转换为字符串

~~~python
a = 10
s1 = str(a)
print(s1)
print(type(s1))

b = 2.5
s2 = str(b)
print(s2)
print(type(s2))

c = None
s3 = str(c)
print(s3)
print(type(s3))

d = False
s4 = str(b)
print(s4)
print(type(s4))

e = True
s5 = str(e)
print(s5)
print(type(s5))

age = 10 # 年龄20岁
s7 = str(age)
print("我今年已经" + s7 + "岁了")
print("我今年已经{age}岁了")
print(f"我今年已经{age}岁了")
~~~

##### rept函数

> repr()函数 将字符串原本的内容完整的进行呈现
>         用于调试代码 找错误的时候 使用     比如我们可以已通过此函数来获取 用户传入的参数 长什么样子

~~~python
s1 = "a\nb"
print(s1)


print(repr(s1))
~~~

##### eval函数

> 执行传入的字符串表达式

~~~python
print(eval("1 + 2"))
print(eval("1 * 2"))
print(eval("1 - 2"))
print(eval("1 / 2"))
print(eval("执行脚本   Linux脚本  Windows脚本  JS脚本  "))
# 不要执行以下代码
# print(eval("_import_(os).system(' format C :')"))
# print(eval("_import_(os).system(' rm rf / :')"))
~~~

##### ord和chr函数

> ASCII
>         0 ~ 127 一共128个字符
>         美国标准信息交换码
>     Unicode
>         0000 ~ FFFF
>         Unicode编码表   万国码    收录了全球各个国家的语言文字   是一个十六进制的编码表
>         一共可以表示65535个文字
>         中文的取值范围是  4E00(19968) ~ 9FA5(40869)

~~~python
print(ord("a"))
print(ord("A"))
print(ord("中"))


print(chr(65))
print(chr(97))
print(chr(20013))

~~~

##### encode和decode函数

>    encode()函数 根据指定的编码格式 进行编码
>     decode()函数 根据指定的编码格式 进行解码
>
> 一个英文字母占几个字节？
>         一个字节
>     一个中文占几个字节？
>         根据不同的编码表 所占字节数不同
>         GB2312 国标标准版    只收录了绝大多数中文简体
>         GBK    2个字节    Guo Biao Kuo Zhan 此编码表只收录了绝大多数中文汉字 简体以及繁体
>         UTF-8    3个字节

~~~python
s1 = "abc中国"
s1_types = s1.encode(encoding="UTF-8")
print(s1_types)
print(type(s1_types))
print(len(s1_types))
s1_new = s1_types.decode("UTF-8")
print(s1_new)

print("-" * 50)

s2 = "abc中国"
s2_types = s2.encode(encoding="GBK")
print(s2_types)
print(type(s2_types))
print(len(s2_types))
s2_new = s2_types.decode("GBK")
print(s2_new)
~~~

##### bool函数

>  bool()函数的使用 将传入的内容  转换为字符串

~~~python
#   bool函数 只要内容非空 或者 不是None 以及其他可以表示为False 的数据  都是True
print(bool("abc"))
print(bool("True"))
print(bool("False"))
print(bool(""))
print(bool("None"))
print(bool(None))
print(bool(123))
print(bool(1.5))
print(bool(0))
print(bool(0.0))
~~~

### 9.输入数据

> 如果需要接收用户在控制台输入的内容 可以使用input函数
>     此函数收到的数据都是在字符串类型

~~~python
name = input("请输入你的名字\n")
print("你输入的名字是",name)

age = int(input("请输入你的年龄\n"))
print("你输入的年龄是",age)
print(type(age))

height = input("请输入你的身高\n")
new_height = int(height)
print("你输入的身高是",height)
print(type(height))

is_happy = input("请输入你今天是否开心True或者False?\n")
print("你输入的是否开心为",is_happy)
~~~

### 10.输出数据

> print()函数用于输出内容 默认打印完以后换行
>     如果不希望打印完之后换行  可以指定end参数的值 来实现打印完之后的效果

~~~python
print(1, end="a")
print(2, end="b")
print(3, end="c")

print("*" * 50)

s1 = "a = %d , b = %f" % (1,2.5678)
print(s1)

print("*" * 50)

s1 = "a = %d , b = %.2f" % (1,2.5678)
print(s1)

s1 = "a = %d , b = %.1f" % (1,2.5678)

print("*" * 50)

# 按照顺序填充参数到字符串中
s2 = "a = {} , b = {} , c = {}".format(10,20,True)
print(s2)

print("*" * 50)
# 按照我们指定的下标顺序 填充参数到字符串中 0表示第一个 1表示第二个 以此类推
s3 = "a = {0} , b = {2} , c = {1}".format(10,20,True)

print("*" * 50)

s4 = "a = {a1} , b = {b2} , c = {c1}".format(a1=1,b2=1,c1=2)
print(s4)

float1 = 31415.9
# : 按照后边的规则进行格式化
# *：以 * 填充空白，不写则默认以空格填充
# ^: 可选 < 、 ^ 、> , 分别对应左对齐、居中、右对齐
# 20: 数字宽度为20，数字长度不足20则进行填充
# .2f: 小数点后保留2位
str2 = "{:*^20,.2f}".format(float1)
print(str2) # *****31,415.90*****

print("*" * 50)

s5 = "字符串的内容{0}".format("abc")
print(s5)

s6 = "{{0}}位置的内容为{0}".format("abc")
print(s6)

print("*" * 50)
a = 1
b = 2
c = 3
print(f"{a},{b},{c}")
print(f"{a=},{b=},{c=}")

# 嵌套括号 将不再有变量值填充的效果
print(f"{{a=}},{{b=}},{{c=}}")

~~~

