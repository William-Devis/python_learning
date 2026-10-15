"""
    多行注释 本质为实现字符串
"""


def dog (name:str, age:(1, 99),species:'狗狗的品种') -> tuple:
    """
    这个用来解释函数的注释
    :param name:
    :param age:
    :param species:
    :return:
    """
    print(name , age , species)
    return True

dog(123,"abc",True)

print(dog.__annotations__)

help(dog)