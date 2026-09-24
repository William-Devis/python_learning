"""
    break关键字 用于循环中 表示中断循环 为执行的循环次数 不再执行

    break中断循环 如果循环后有else关键字 也将不再执行 因为else也属于循环结构的一部分

"""

# 需求：模拟跑步10圈 跑完7圈 太累了退出

for i in range(1,11):
    if i == 8:
        break
    print(f"跑步第{i}圈")
else:
    print("跑步结束了")

print("程序结束")