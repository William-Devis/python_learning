"""
    使用with关键字可以更加简洁优雅的处理资源
"""

try:
    with open("a.txt", "r", encoding="utf-8") as reader:
        print(reader.read())
except OSError as e:
    print(e)
finally:
    print(reader.closed)

print("---------------------------------------------------------------------")

with open("a.txt", "r", encoding="utf-8") as reader:
    print(reader.read())

