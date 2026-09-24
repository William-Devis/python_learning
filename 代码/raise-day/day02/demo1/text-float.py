"""
    float类型属于浮点数类型 小数类型 是有精度损失的    任何语言 只要采用的时IEEE754的这个标准定义的类型
    都有这个问题 因为CPU采用这个标准 所以计算机语言采用相同的标准 运算效率更高 但是精度无法保证
    如果需要存在货币 进行科学计算 等对精度有要求的情况下 可以使用Decimal 类 此类使用字符串的方式
    来记录任何精度 任何大小的数据 并且数据的准确度 不存在任何误差
"""

a = 0.1
b = 0.2
print(a + b) # 0.30000000000000004 精度缺失
print(type(a))
print(type(b))

# 从名为decimal的模块中导入了Decimal这个类
from decimal import Decimal
a = Decimal("0.3432524254535")
b = Decimal("0.6757456645646")
print(type(a))
print(type(b))
print(a + b)
print(a * b)
print(a / b)