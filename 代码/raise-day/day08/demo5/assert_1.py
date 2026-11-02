"""
    assert 断言 处理异常
    assert 后边跟一个表达式
        如果条件成立 则无事发生
        如果条件不成立 则Python解释器会自动创建一个异常对象AssertionError类型 我们自行添加异常信息即可
"""


def get_sum(num1, num2):
    assert isinstance(num1, (int,float)) and isinstance(num2, (float,int)) , "类型不符合，必须为int或者float"
    return num1 + num2

try:
    print(get_sum("abc", 2))
except AssertionError as e:
    print(e)

print("程序结束")