"""
    使用多个except捕获不同类型的异常
"""


try:
    num_1 = int(input("请输入被除数\n"))

    num_2 = int(input("请输入除数\n"))

    print(num_1 / num_2) # Python中除法  默认为float类型

except ValueError as e:
    print("捕获到了值异常",e)
except ZeroDivisionError as e:
    print("捕获到了除数为零异常",e)

print("程序结束")

