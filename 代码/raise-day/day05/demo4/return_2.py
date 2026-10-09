"""
    return关键字的其他用法
"""

def is_even(num):
    # if num % 2 == 0:
    #     return "偶数"
    # else:
    #     return "奇数"

    return "偶数" if num % 2 ==0 else "奇数"

print(is_even) # 只写函数名 属于打印函数对象 展示函数的基本信息
print(is_even(10)) # 调用函数 并且得到返回值交给print函数打印
print(is_even(11)) # 调用函数 并且得到返回值交给print函数打印


def is_even1(num):
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False
    return num % 2 == 0
print(is_even(10)) # 调用函数 并且得到返回值交给print函数打印
print(is_even(11)) # 调用函数 并且得到返回值交给print函数打印

def is_even2(num):
    # if num % 2 == 0:
    #     return 0
    # else:
    #     return 1
    return num % 2

print(is_even2(10)) # 调用函数 并且得到返回值交给print函数打印
print(is_even2(11)) # 调用函数 并且得到返回值交给print函数打印

print("-------------------------------------------------------")

def func():
    for i in range(10):
        if i == 8:
            return # 注意和break的区别
        print(i)
    print("func函数执行完毕")

func()







