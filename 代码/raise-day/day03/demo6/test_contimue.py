"""
    continue关键字作用于循环中 用于跳过本次循环中未执行的代码 开始下一次新的循环
    continue关键字通常结合分支结构一起使用

    shift + alt + ↓↑ 移动当前行代码

"""

# 打印1~10 如果打印到5跳过 继续打印后续的内容

for i in range(1,11):
    if i == 5:
        print("跳过5不打印")
        continue
        print("hello continue") # 不可达代码 因为遇到continue即会开始一次新的循环 所以写在这里是无效的 无意义的
    print(i)

print("*" * 50)

# 模拟跑步10圈 跑到第八圈 太累了 休息一圈 继续跑

for i in range(1,11):
    if i == 8:
        print("太累了,休息一圈")
        continue
    print(f"跑步第{i}圈")