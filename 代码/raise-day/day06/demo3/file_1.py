"""
    写入文件
    写入文件的时候 如果文件不存在 会自动创建一个
    写的时候指定模式 w 或者 a
    w write 会覆盖原文件中的内容
    a append 在原文件的基础上追加内容
"""
writer = open("D.txt","a",encoding="utf-8")

writer.write("123 456")

writer.flush() # 刷新缓存 将缓存中的数据刷新到硬盘中

writer.close() # 关闭资源


