"""
    递归: recursive 递归和回归

    简单的理解: 函数自己调自己

    准确的理解：
    一个大的问题可以通过逻辑拆分为若干个小的问题 可以通过一个函数自己调用当前函数实现
    必须有结束的条件(递归的出口)

    举例：
    赵四  广坤  小宝  富贵  大拿



    递归的实际应用:
        求 1 ~ n之和
        求阶乘
        很多算法都会用到递归 快排 归并
        斐波那契数列
        八皇后算法
        遍历文件
        汉诺塔问题
"""

# def func1():
#     func1()
#
# func1() 这段代码 报错 因为没有结束条件

print("--------------------------求1~5之和--------------------------")

def get_num5():
    return 5 + get_num4()

def get_num4():
    return 4 + get_num3()

def get_num3():
    return 3 + get_num2()

def get_num2():
    return 2 + get_num1()

def get_num1():
    return 1

print(get_num5())

print("-------------------------求1~n之和 递归实现--------------------------")

def get_sum(num):
    if num == 1:
        return 1
    return num + get_sum(num - 1)

print(get_sum(5))

print("-------------------------求1~n之和 递归实现--------------------------")

def get_factorial(num):
    if num < 1 or num == 1:
        return 1
    return num * get_factorial(num - 1)

print(get_factorial(5))







