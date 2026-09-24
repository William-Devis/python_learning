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