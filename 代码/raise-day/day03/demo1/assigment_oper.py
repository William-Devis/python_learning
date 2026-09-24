"""
    赋值运算符
    =
    +=
    -=
    *=
    /=
    //=
    %=
    **=
    :=
"""

a = 10
print(a)

a += 5 # 等同于 a = a + 5
print(a)
a -= 5 # 等同于 a = a - 5
print(a)
a *= 5 # 等同于 a = a * 5
print(a)
a /= 5 # 等同于 a = a / 5
print(a)
a //= 5 # 等同于 a = a // 5
print(a)

b = 10
b //= 3 # 等同于 b = b // 5
print(b)

a = 2
a **= 3 # 等同于 a = a ** 3
print(a)

print("-" * 50)

# := 海象运算符
c = 10
print(d := 10)

e = 0
print((e :=10) > 5)
print(e)