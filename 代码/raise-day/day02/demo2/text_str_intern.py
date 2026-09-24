"""
    str类型的intern机制
    为了共享str对象 节省内存资源 str类型的对象默认是开启intern机制的
    除非字符串中包含一些特殊的符号 或者 空格等
"""

s1 = "abc"
s2 = "abc"
print(s1)
print(s2)
print(s1 == s2)
print(s1 is s2)
print(id(s1))
print(id(s2))

s3 = "a b c"
s4 = "a b c"
print(s3 == s4)
print(s3 is s4)
print(id(s3))
print(id(s4))