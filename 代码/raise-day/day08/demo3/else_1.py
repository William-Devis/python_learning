"""
    使用else处理异常 else中的代码 表示上方的tru结构 没有出现异常
    将会执行的代码
    else可以提高代码的可读性 可维护性

"""

try:
    num_1 = int(input("请输入被除数\n"))

    num_2 = int(input("请输入除数\n"))

    result = num_1 / num_2

except ZeroDivisionError as e:
    print("捕获到了除数为零异常",e)
except ValueError as e:
    print(e)
else:
    print("{0} / {1} = {2}".format(num_1, num_2, result))

print("程序结束")



