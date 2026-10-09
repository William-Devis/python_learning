"""
    关于参数的传递 底层细节

    在Java语言中分为值传递和引用传递 比如 10 这种数值属于值传递 而 对象这种属于引用传递

    Python中的严格来讲 是没有值传递和引用传递的说法
    因为在Python中所有的数据全部属于对象 都属于引用传递
    在函数体内对参数的修改是否会影响原变量 完全取决于是可变类型 还是 不可变类型
"""

def func1(a):
    a += 1
    print("func1函数中a的取值:",a)

b = 10
func1(b)
print("实参参数b的取值:",b)

print("-----------------------------------------")

def func2(nums):
    nums[0] += 1
    print("func2函数中nums的取值为:",nums)

list1 = [1,2,3]
func2(list1)
print("list1的元素值为:",list1)

print("-----------------------------------------")

# 直接将一个列表赋值给另外一个列表 属于直接将堆内存中的地址值进行了复制

def func3(nums):
    nums[0] += 1
    print("func3函数中nums的取值为:",nums)

list1 = [1,2,3]
list2 = list1
func3(list2)
print("list1的元素值为:",list1)
print("list2的元素值为:",list2)

print("-----------------------------------------")

# 深拷贝 从外到内 都创建新的对象

import  copy
list1 = [1,2,3]

list2 = copy.deepcopy(list1)

func2(list2)
print("list1的元素值为:",list1)
print("list2的元素值为:",list2)

print("-----------------------------------------")

# 浅拷贝 外层的列表 复制全新 里边的元素 用的是同一个

list1 = [1,2,3]

list2 = list1.copy()

list3 = list1[:]

print(id(list1),id(list2),id(list3))