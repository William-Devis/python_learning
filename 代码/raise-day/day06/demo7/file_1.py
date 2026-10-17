"""
    读取一行  或者 多行文本内容
    readline()   读取一行
    readlines() 读取所有行
"""

reader = open("A.txt","r",encoding="utf-8")

# print(reader.readline(),end="")
# print(reader.readline(),end="")
# print(reader.readline(),end="")
# print(reader.readline(),end="")
# print(reader.readline(),end="")
# print(reader.readline(),end="")

print(reader.readlines(38))