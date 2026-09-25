"""
    继续优化：可以让调用者灵活的控制符号数量

    通过参数实现：函数的调用者与函数的定义之间传递的数据 称之为参数
        形参：形式参数 函数定义的时候书写的参数 属于形参
        实参：实际参数 函数调用的时候传入的参数 属于实参

    定于了形参以后 必须传入对应个数的实参 除非形参有默认值 否则运行报错
"""

def print_sign(num):
    for _ in range(num):
        print("-", end="")
    print()


print("床前明月光")
print_sign(7)

print("疑是地上霜")
print_sign(10)

print("举头望明月")
print_sign(20)

print("低头思故乡")
print_sign(85)