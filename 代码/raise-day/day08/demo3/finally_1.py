"""
    finally中用于书写 不管是否出现异常 以及 异常是否被捕获到 都将执行的代码
"""


try:

    list1 = [1,2,3]

    print(list1[3])

    num_1 = int(input("请输入被除数\n"))

    num_2 = int(input("请输入除数\n"))

    result = num_1 / num_2

except ZeroDivisionError as e:
    print("捕获到了除数为零异常",e)
except ValueError as e:
    print(e)
else:
    print("{0} / {1} = {2}".format(num_1, num_2, result))
finally:
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        print(e)


    print("程序结束")

