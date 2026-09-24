"""
    if-else结构 根据条件选择执行if结构内或者else结构内的代码
    条件成立了 执行if结构内代码
    条件不成立 执行else结构内代码
    必须二选一
"""

age = int(input("请输入你的年龄\n"))
if age >= 18:
    print("你成年了")
else:
    print("未成年")

print("程序结束")