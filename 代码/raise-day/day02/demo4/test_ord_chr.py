"""
    ASCII
        0 ~ 127 一共128个字符
        美国标准信息交换码
    Unicode
        0000 ~ FFFF
        Unicode编码表   万国码    收录了全球各个国家的语言文字   是一个十六进制的编码表
        一共可以表示65535个文字
        中文的取值范围是  4E00(19968) ~ 9FA5(40869)

"""

print(ord("a"))
print(ord("A"))
print(ord("中"))


print(chr(65))
print(chr(97))
print(chr(20013))
