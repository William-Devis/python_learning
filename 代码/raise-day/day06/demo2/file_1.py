"""
    读文件
    当我们读取文件 默认的读取文件的编码格式 是按照本地平台(操作系统)默认的编码格式读取的
    比如 中文操作系统 将以GBK编码格式读取
"""

# "C:\\Users\\WHD\\Desktop\\A.txt"
# reader = open("C:/Users/WHD/Desktop/A.txt","r",encoding="utf-8")
reader = open("C:/Users/WHD/Desktop/A.txt","r")

print(reader.read())

reader.close() # 关闭资源 关闭流

