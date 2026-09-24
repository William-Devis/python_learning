"""
    小整数池    CPython解释器将-5 ~ 256 这个范围的整数 存在小整数池    当我们声明变量
    取值属于这个范围的数据    将直接使用小整数池中的对象   不会重复创建多个对象
    这样设计的目的   是为了节省内存资源

    在终端通过交互式的方式可以直接感受上方的描述 如果在Pycharm中 因为Pycharm对整数的存储也做了优化
    所以不需要记忆 按照CPython解释器的规则来记忆即可
    Java语言也有这样的设计   将Byte有符号取值范围(-128 ~ 127)内的数据 存放在一个 缓存数组中 CacheArray

    因为不可变 才可以共享
"""

a = 10
b = 10
c = 10
print(a)
print(b)
print(c)

# 呈现内存中的地址值
print(id(a))
print(id(b))
print(id(c))

# 通过is关键字 比较是否属于同一个对象 注意：严格比较内存地址
print(a is b)
print(a is c)
print(b is c)

print("--------------------------")

a = 300
b = 300
c = 300
print(id(a))
print(id(c))
print(id(b))

print(a is b)
print(b is c)
print(a is c)

# 以上代码在终端中执行 观察效果