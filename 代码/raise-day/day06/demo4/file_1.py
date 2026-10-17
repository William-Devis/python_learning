"""
    读写二进制文件

    读取的模式 rb read binary
    写入的模式 wb write binary
"""

reader = open("C:\\Users\\WHD\\Desktop\\资料\\zs.jpg","rb")

read_data = reader.read()

writer = open("copy.png","wb")

writer.write(read_data)

reader.close()
writer.close()




