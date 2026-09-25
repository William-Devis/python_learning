"""
    关于参数的传递细节

        解包传参
"""

def func(a,b,c):
    print(a,b,c)

func(1,2,3)
func(a=1,b=2,c=3)
func(1,2,c=3)

list1 = [2,1,3]
func(*list1)

tuple1 = (2,1,3)
func(*tuple1)

set1 = {2,1,3}
func(*set1) # 实际工作中不用 因为顺序无法保证

# 字典解包传参 其实是为了处理关键字参数
# 所以 字典中的键的名字必须和形参的名字完全一致 对照 数量相同
# 顺序无所谓 因为关键字参数 本身就没有顺序要求
dict1 = {"a":1,"b":2,"c":3}
func(**dict1)
func(b = 2,a = 1,c = 3)