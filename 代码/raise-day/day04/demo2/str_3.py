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