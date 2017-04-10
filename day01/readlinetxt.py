# -*- coding: UTF-8 -*-
# 以只读模式打开文件hello.txt
f = open("hello.txt","r")
# 读取第一行
c1 = f.readline()
# 读取第二行
c2 = f.readline()
# 读取第三行
c3 = f.readline()
# 关闭文件
f.close()
# 输出读取文件第一行内容
print(c1)
# 输出读取文件第二行内容
print(c2)
# 输出读取文件第三行内容
print(c3)