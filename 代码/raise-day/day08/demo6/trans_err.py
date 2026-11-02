"""
    异常的传递 ： 嵌套结构中 内层的异常 会先由内层结构处理
    如果可以处理 则异常处理结束 否则层层向外传递 直到处理完毕 或者 嵌套结构结束
"""
try:
    try:
        try:
            print(10 / 0)
        except ValueError  as e:
            print("最内层的except处理异常：",e)
    except ZeroDivisionError  as e:
        print("中间层的except处理异常：", e)
except NameError as e:
    print("最外层的except处理异常：", e)


print("程序结束")