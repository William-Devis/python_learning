"""
    str类型 字符串类型
    任何被英文双引号或者单引号包括的内容 都属于字符串的实例 也就是对象

    Literal 字面量 对于字符串而言 直接书写在双引号或者单引号之内 这个值属于字面量 属于与字面量
    字面量都属于常量 常量不能修改
"""
from email.errors import ObsoleteHeaderDefect

s1 = "abc"
s2 = "ABC"
s3 = "hello world"

print(s1)
print(s2)
print(s3)
print(s1 + s2 + s3) # 字符串的加法计算属于拼接字符串

print(type(s1))
print(type(s2))
print(type(s3))


html_str = "<html>\
       <head>\
          <title>这是我的第一个网页</title>\
       </head>\
       <body>\
       网页的内容......\
       </body>\
</html>"

html_str2 = """<html>
       <head>
          <title>这是我的第一个网页</title>
       </head>
       <body>
            网页的内容......
       </body>
</html>"""

print("*" * 50)

s1 = "\\\\"
print(s1)

s2 = "\""
print(s2)

s3 = "'"
print(s3)

s4 = "\'"
print(s4)

s5 = '\''
print(s5)

s6 = "abc\bdef" # 退格
print(s6)

s7 = "a\nb\nc" # 换行
print(s7)

# 制表符
s8 = "床\t\t前\t明\t月\t光"
s9 = "疑\t\t是\t地\t上\t霜"
print(s8)
print(s9)

# 注意 \r 只是回车的效果 即回到行首
s10 = "abc\rdef"
print(s10)