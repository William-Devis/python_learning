"""
    read()函数是有计数指针的 每一次读取都从上次一次读取的末尾继续
"""

reader = open("../A.txt","r",encoding="utf-8")

print(reader.read(1))
print(reader.read(1))

reader.close()
