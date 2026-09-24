"""
    for循环用于遍历可迭代对象 次数是固定的
    在Python中 字符串属于可迭代对象
"""

for i in "hello world":
    print(i)

print("*" * 50)

for i in [1,3,5,77,36,74,245]:
    print(i)

print("*" * 50)

print(range(10))

print("*" * 50)
# range()函数 如果只写一个参数 表示stop 即结束值 从0开始 到stop -1 结束
for i in range(10):
    print(i)

print("*" * 50)
# 书写两个参数 从前往后 分别为start 以及stop
for i in range(1,10):
    print(i)

print("*" * 50)
# 如果书写三个参数 分别表示 start stop 以及 step 步长默认为1 可以根据需求自行设定
for i in range(1,10,3):
    print(i)

print("*" * 50)
# 包括起始位置-10   不包括结束位置10   左闭右开
for i in range(-10,10):
    print(i)

print("*" * 50)

# 如果要将序遍历 则步长必须设定为负数
for i in range(10,-10,-1):
    print(i)
