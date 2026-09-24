"""
    逻辑运算符
    and 并且 两个条件必须都成立 则结果为True 如果前边的条件不成立 则直接返回False   后边的不再执行  短路效果
    or 或者 有一个条件为True 则结果为True 如果前边的条件成立 则直接返回True 后边的不再执行 短路效果
    not 取反 非True 即False     非False即True
"""
b1 = True
b2 = False
b3 = True
print(b1 and b2)
print(b2 and b3)
print(b1 and b3)

print("*" * 50)

a = 10
b = 20
c = 30
print((a < b) and (b < c))

print("*" * 50)

print(1 and 2) # 如果第一个为True 则返回第二个
print(0 and 3) # 如果第一个为False 则返回第一个

print("*" * 50)

b1 = True
b2 = False
b3 = True
print(b1 or b2)
print(b2 or b3)
print(b1 or b3)

print("*" * 50)

a = 10
b = 20
c = 0
print((a < b) or (c:=100) > b)
print(c)

print("*" * 50)

print(1 or 2) # 如果第一个为True 则返回第一个
print(0 or 3) # 如果第一个为False 则返回第二个

print("*" * 50)

print(not 1)
print(not 0)
print(not False)
print(not True)