"""
    如果需要接收用户在控制台输入的内容 可以使用input函数
    此函数收到的数据都是在字符串类型
"""

name = input("请输入你的名字\n")
print("你输入的名字是",name)

age = int(input("请输入你的年龄\n"))
print("你输入的年龄是",age)
print(type(age))

height = input("请输入你的身高\n")
new_height = int(height)
print("你输入的身高是",height)
print(type(height))

is_happy = input("请输入你今天是否开心True或者False?\n")
print("你输入的是否开心为",is_happy)