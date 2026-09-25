"""
    关于参数的传递细节
        位置参数
        关键字参数
        解包传参
"""

def print_sign(num,sign):
    for _ in range(num):
        print("-", end="")
    print()


print("床前明月光")
print_sign(7,"^") # 位置参数 严格按照位置的顺序传入

print("疑是地上霜")
print_sign(10,"&")

print("举头望明月")
print_sign(sign = "&",num = 10)

print("低头思故乡")
print_sign(8,"*")


# print_sign(num = 8,"*") 不能这样书写 报错 关键字参数必须再位置参数后边
