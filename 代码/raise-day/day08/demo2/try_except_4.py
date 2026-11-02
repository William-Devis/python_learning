"""
    使用一个 except 处理多个不同类型的异常
    将多个异常书写在一个元组中即可
"""


try:
    num_1 = int(input("请输入被除数\n"))

    num_2 = int(input("请输入除数\n"))

    print(num_1 / num_2) # Python中除法  默认为float类型

except (ValueError,ZeroDivisionError) as e:
    print("捕获到了异常",e,type(e))

print("程序结束")

