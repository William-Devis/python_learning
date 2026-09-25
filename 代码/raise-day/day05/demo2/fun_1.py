"""
    可变长参数   以及 默认值参数
"""

def func1(a,*nums):
    print(a,nums)

func1(1,2,3,4,5)
func1(1,2)

# 如果在可变长参数之后还有参数 必须通过关键字参数的方式 进行传递
def func2(a,*num3,b):
    print(a,*num3,b)

func2(1,2,3,4,5,b = 6)

def func3(a=1,b=True):
    print(a,b)

func3()
func3(2,False)