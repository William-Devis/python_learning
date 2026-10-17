"""
    __del__() 当当前对象被垃圾回收 将自动调用此函数
"""

class Student:

    def __del__(self):
        print(f"当前对象被垃圾回收了,id为哦：{id(self)}")


s1 = Student()

s2 = s1

del s1

print("程序结束")
