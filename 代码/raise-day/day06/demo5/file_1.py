"""
    读写文件的优化操作 我们之前的read() 无参 都是一次性将文件全部读取进来的
    文件小没有问题 如果文件非常大 这样是非常不合适的 我们应该少量多次的循环读取 直到读取完毕
        read(整数数值参数)
        如果是文本文件 数值表示字符数
        如果是二进制文件 数值表示字节
"""


def copy_file(src_file, dst_file):
    reader = open(src_file,"rb")
    writer = open(dst_file,"wb")

    while content := reader.read(1024):
        writer.write(content)
    reader.close()
    writer.close()


copy_file("C:\\Users\\WHD\\Desktop\\资料\\zs.jpg","new_zs.jpg")

