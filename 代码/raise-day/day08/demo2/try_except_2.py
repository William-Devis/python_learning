"""
    使用try-except处理异常
    try：结构内用于书写可能出现异常的代码
    except：用于捕获异常

    try或者except不能单独使用
        try-except
        try-except-else
        try-except-finally
        try-except-else-finally

    直接输出对象 相当于调用此对象的__str__函数
"""


try:
    num_1 = int(input("请输入被除数\n"))

    num_2 = int(input("请输入除数\n"))

    print(num_1 / num_2) # Python中除法  默认为float类型

except ValueError as e:
    print("捕获到了值异常",e)

print("程序结束")

