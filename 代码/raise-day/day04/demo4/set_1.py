"""
    集合的创建方式
    集合是无序的，且不包含重复的元素。
    集合使用 {} 定义，数据之间使用 ，分隔，也可以使用set()定义。
    集合没有索引，所以不能通过切片的方式访问集合元素。
    集合中元素可以是不同的类型。
    集合可以进行数学上的集合操作，如并集、交集和差集。
    集合适用于需要快速成员检查、消除重复项和集合运算的场景。
"""

set1 = {1,2,3,4,5,6}
print(set1)
print(type(set1))

set2 = set([1,2,3,4,5,6])
print(set2)
print(type(set2))

set3 = set()
print(set3)
print(type(set3))

set4 = {}
print(set4)
print(type(set4)) # 这种是字典 注意

set5 = {x for x in range(5)}
print(set5)
print(type(set5))