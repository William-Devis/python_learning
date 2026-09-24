"""
    数值的各种进制写法
"""

# 二进制 0b 或者 0B
a = 0B111
print(a)

# 八进制
b = 0o11
print(b)

# 十进制
c = 11
print(c)

# 十六进制 0X 或者 0x
d = 0X4E2D
print(d)

print("-" * 50)

num = 20
print("十进制", num)
print("二进制", bin(num))
print("八进制", oct(num))
print("十六进制", hex(num))

e = None # 当我们不确定一个变量的值为多少时，可以先赋值为None

a = 1223352544364535235235234

num1 = 1_000_000_000_000_000
print(num1)