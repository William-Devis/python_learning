"""
    继续优化：可以让调用者灵活的控制符号数量 以及 符号的类型

    对于函数定义的时候，参数的数量结合具体需求定义即可，没有限制
"""

def print_sign(num,sign):
    for _ in range(num):
        print("-", end="")
    print()


print("床前明月光")
print_sign(7,"A")

print("疑是地上霜")
print_sign(10,"&")

print("举头望明月")
print_sign(2,"hello")

print("低头思故乡")
print_sign(8,"*")