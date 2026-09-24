"""
    encode()函数 根据指定的编码格式 进行编码
    decode()函数 根据指定的编码格式 进行解码


    一个英文字母占几个字节？
        一个字节
    一个中文占几个字节？
        根据不同的编码表 所占字节数不同
        GB2312 国标标准版    只收录了绝大多数中文简体
        GBK 2个字节    Guo Biao Kuo Zhan 此编码表只收录了绝大多数中文汉字 简体以及繁体
        UTF-8 3个字节
"""

s1 = "abc中国"
s1_types = s1.encode(encoding="UTF-8")
print(s1_types)
print(type(s1_types))
print(len(s1_types))
s1_new = s1_types.decode("UTF-8")
print(s1_new)

print("-" * 50)

s2 = "abc中国"
s2_types = s2.encode(encoding="GBK")
print(s2_types)
print(type(s2_types))
print(len(s2_types))
s2_new = s2_types.decode("GBK")
print(s2_new)

