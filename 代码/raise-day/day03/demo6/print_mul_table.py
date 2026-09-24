"""
    使用嵌套for循环打印乘法表
    外层循环控制行数 一共有9行
    内层循环控制列数 每一行的列数与行数相同

    嵌套循环 外层循环变化一次 内层循环变化一轮

    程序调试 debug 是通过让代码逐行执行的方式排查问题的常用手段
    在需要代码停止的位置 单机打断点/取消断点   右键 以debug模式执行
    表示代码将停止在这一行 观察变量的变化 以及 控制台的变化
"""


for i in range(1,10):
    for j in range(1,i + 1):
        print(f"{i} * {j} = {i * j}",end="\t")
print()

print("程序结束")

for a in range(1,6):
    for b in range(1,6):
        print("*",end="\t")
    print()