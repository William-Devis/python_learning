"""
    元组的遍历
"""

print("-------------元组遍历--------------")

tuple1 = (1,22,33,4,55,6,)

for i in tuple1:
    print(i)

print("-------------len函数遍历--------------")

for i in range(len(tuple1)):
    print(i,tuple1[i])

print("-------------enumerate遍历--------------")

for i ,v in enumerate (tuple1,start=1): # 指定start 表示序号从1开始 注意 还是从下标为0的元素遍历的
    print(i,v)