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