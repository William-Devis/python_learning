"""
    with关键字 属于语法糖 就是为了简化对于资源的管理 所要编写的 try except finally等 模板代码
    Python中的IO相关的异常 统一由OSError来处理
"""

try:
    reader = open("a.txt", "r", encoding="utf-8")
    print(reader.read())

    print(10 / 0)

except OSError as e:
    print(e)
finally:
    reader.close()
    print(reader.closed)



