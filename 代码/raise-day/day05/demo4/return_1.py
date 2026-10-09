"""
    有些函数在执行的时候，需要有返回值给调用者，通过return关键字进行返回，返回到函数调用的位置。

    需求：编写函数计算两个函数之和 在函数之外判断最终的结果是奇数还是偶数

    return 用于在函数体内返回结果 返回给函数的调用者
    return表示结束函数并且返回内容

"""

def my_sum(a,b):
    result = a + b
    print("a与b之和为：",result)

get_data = my_sum(2,2)

print(get_data)

if 4 % 2 == 0:
    print("偶数")
else:
    print("奇数")

# 以上代码可以实现求和 但是 无法在后续的代码中利用最终的和 所以无法进行判断 相当于逻辑无法串联
# 如何让解决以上问题?使用return关键字 返回值实现


print("-----------------------------------------------------------")


def my_add(a,b):
    result = a + b
    print("a与b之和为:",result)
    return result
    print("函数继续运行") # 在Java代码中这里就报错 但是在Python中不报错 但同样永远执行不到

get_sum = my_add(24324,4)

if get_sum % 2 == 0 :
    print("偶数")
else:
    print("奇数")