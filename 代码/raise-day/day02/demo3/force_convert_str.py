"""
    str函数 将传入的数据转换为字符串
"""

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