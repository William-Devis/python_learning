"""
    数据类型和类型的判断
    Type() 返回数据对应类型
    isinstance() 判断某个数据是否属于某个类型的实例(对象)
    instance 实例 对象就是实例

    bool类型在Python也属于数据类型int 在有些情况下 可以当做数值使用 因为bool继承了int
"""

a = 10
print(type(a))
b = 2.5
print(type(b))
c = True
print(type(c))
d = False
print(type(d))
e = "abc"
print(type(e))

# 严格比较是否为同一个类型
print(type(c) == type(a))

print("-" * 50)

# 不仅会比较同类型 还会比较父类类型
print("a是否为int类型",isinstance(a, int))
print("b是否为int类型",isinstance(b, int))
print("c是否为int类型",isinstance(c, int))
print("d是否为int类型",isinstance(d, int))
print("c是否为bool类型",isinstance(d, bool))
print("d是否为bool类型",isinstance(d, bool))
print("e是否为int类型",isinstance(e, int))