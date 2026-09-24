"""
    变量的定义

    变量是用于存储数据的 Python中的变量直接声明赋值即可  类型是由数据决定的

    编码规范：运算符左右两边必须空格    不能紧凑在一起写

    ctrl + alt + l ：自动对齐格式化代码

    如果你看到自定义的内容下方有虚线 可以查看 如果提示 shadows    name ...... 表示自定义的名称和官方的命名重复了 推荐换一个别的名字

    tab键根据PyCharm提示补全

    控制台程序结束状态码0    表示程序正常运行完毕 没有错误  否则表示程序出错

    Ctrl + / 注释多行选中的代码
"""
import keyword
print(keyword.kwlist)

a = 10
b = 20
result = a + b
print(result)

print("-------------------------------------------------")
print("-" * 50)

name = "赵四"
age = 20
weight = 75.5
print(name)
print(age)
print(weight)
print(name, age, weight)

print("-" * 50)

var1 = var2 = var3 = 100
print(var1, var2, var3)
c, d, e, = 5, 6, 7
print(c, d, e)

a1 = 6
# &b = 5
# 6@ = 4
变量 = 9
print(a1, 变量)