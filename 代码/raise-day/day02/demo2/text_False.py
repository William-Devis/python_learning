"""
    在开发中 一些特殊的值或者空容器 也可以表示为False
    None 0 0.0 "" [] () {}
     None也被设计为全局单例对象 即同一个Python进程中 所有的None对象都是同一个 也是为了节省内存资源
"""

if not None:
    print("条件成立1")

if not 0:
    print("条件成立2")

if not 0.0:
    print("条件成立3")

if not []:
    print("条件成立4")

if not ():
    print("条件成立5")

if not {}:
    print("条件成立6")

a = None
print(a == False)
print(a is False)

b = None
c = None
d = None
print(a == b)
print(a == c)
print(a == d)
print(a is b)
print(a is c)
print(a is d)

print("程序结束")