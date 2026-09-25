"""
    函数即一系列代码指令的集合   用于解决特定的问题   可以反复调用
    必须先定义 再使用
"""

# 以下代码 虽然可以实现需求 但是书写非常啰嗦 代码存在 冗余
print("床前明月光")

print("--------------")

print("疑是地上霜")

print("--------------")

print("举头望明月")

for _ in range(10):
    print("-",end="")
print()

print("低头思故乡")
for _ in range(10):
    print("-",end="")
print()