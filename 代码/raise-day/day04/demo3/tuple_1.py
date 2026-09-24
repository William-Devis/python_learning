"""
    元组的创建
    元组是一个不可变的、有序的元素集合。
    不能对元组中的元素进行修改操作。
    元组使用 () 定义，数据之间使用，分隔。
    元组中每个元素都有对应的位置值，称为索引或下标，索引从起始从0开始向后逐个递增，并且末尾从-1开始逐个向前递减。
    元组中元素可以是不同的类型。
    元组的使用方式与列表类似
"""

print("*****************元组的创建***************")
tuple1 = (1,22,33,4,55,6,)
print(tuple1)
print(type(tuple1))

tuple2 = (1,) # 如果只有一个元素 必须加上逗号
print(tuple2)
print(type(tuple2))

print("*****************元组的创建 元组推导式***************")
list1 = (x for x in range(1,11))
print(list1)
gen_obj = (x for x in range(1,11) if x % 2 == 0) # 这里返回值为生成器对象
print(gen_obj)
tuple3 = tuple(gen_obj) # 结合tuple函数 创建tuple对象
print(tuple3)

