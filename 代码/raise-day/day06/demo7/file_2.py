"""
    walk()函数 用于文件遍历
    os.getcwd()
"""

import os

for root , dir_name , file_name in os.walk("C://"):  # os.getcwd() 表示当前位置
    print("当前位置：",root)
    print("文件夹名称：",dir_name)
    print("文件名称：",file_name)

