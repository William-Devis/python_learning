"""
    因为所有的异常都继承自Exception 所以如果在except后边书写了 Exception
    那么将可以处理所有的异常 但是不推荐这样书写 因为代码可读性较差

    如果要书写多个exception处理多种异常 异常的书写顺序为先写子类 再写父类

"""


try:
    num_1 = int(input("请输入被除数\n"))

    num_2 = int(input("请输入除数\n"))

    print(num_1 / num_2) # Python中除法  默认为float类型

except  Exception  as e:
    print("第一个except处理异常",e)
except ZeroDivisionError as e:
    print("捕获到了除数为零异常",e)
except ValueError as e:
    print(e)


print("程序结束")

