"""
    复数函数 complex()

    数学中使用i表示虚部 Python中使用1j表示
    因为在电气工程学领域i表示电流符号 所以在Python特意避免歧义 避免混淆


"""

c1 = complex(1,2)
print(c1)
print(c1.real)
print(c1.imag)


c2 = complex("1+2j")
print(c2)
print(c2.real)
print(c2.imag)