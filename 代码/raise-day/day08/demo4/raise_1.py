"""
    raise 用于抛出(创建)异常对象
    用于在合适的时机 结束程序 由于代码中出现了严重的错误 而应该停止程序
"""


def get_sum(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 + num2
    else:
        raise TypeError("类型不符合，必须为int或者float")

try:
    print(get_sum("abc", 2))
except TypeError as e:
    print(e)

print("程序结束")
