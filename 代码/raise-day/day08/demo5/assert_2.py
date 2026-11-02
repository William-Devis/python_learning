"""
    使用多个assert来处理程序中的异常
"""


def get_sum(num1, num2):
    assert isinstance(num1, (int,float)) , f"num1类型不符合,输入的内容为:{repr(num1)}，必须为int或者float"
    assert isinstance(num2, (float,int)) , f"num2类型不符合,输入的内容为:{repr(num2)}，必须为int或者float"
    return num1 + num2

try:
    print(get_sum( 2,"ab\t\nc"))
except AssertionError as e:
    print(e)

print("程序结束")