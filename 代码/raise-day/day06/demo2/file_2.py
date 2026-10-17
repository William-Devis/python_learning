"""
    使用相对路径读取文件
"""

reader1 = open("C.txt","r",encoding="utf-8")

print(reader1.read())

reader1.close()

print("-----------------------------------------------------------------")

reader2 = open("./C.txt","r",encoding="utf-8")

print(reader2.read())

reader2.close()

print("-----------------------------------------------------------------")

reader3 = open("../A.txt","r",encoding="utf-8")

print(reader3.read())

reader3.close()

print("-----------------------------------------------------------------")

reader4 = open("C:\\Users\\WHD\\PycharmProjects\\AI0525\\day06\\A.txt","r",encoding="utf-8")

print(reader4.read())

reader4.close()

print("-----------------------------------------------------------------")

reader5 = open("../../B.txt","r",encoding="utf-8")

print(reader5.read())

reader5.close()




