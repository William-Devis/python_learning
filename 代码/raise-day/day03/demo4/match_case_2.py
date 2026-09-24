"""
    使用match-case根据月份统计当月天数
"""

match month := 14:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"{month}月有31天")
    case 4 | 6 | 9 | 11:
        print(f"{month}月有30天")
    case 2:
        print(f"{month}月有28天")
    case _:
        print("月份输入错误")

print("程序结束")

print("-" * 50)

# 三目运算符 三元运算符
a = 10
b = 20
c = 100 if a > b else 200
print(c)

age = 18
print("成年了" if age >= 18 else "未成年")
# 后续在返回值的位置 使用三目运算符 也是很常见的做法 可以简化代码