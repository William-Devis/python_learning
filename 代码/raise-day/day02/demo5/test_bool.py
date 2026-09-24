"""
    bool()函数的使用 将传入的内容  转换为字符串
"""

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