# -*- coding: UTF-8 -*-
# 以只读的方式打开文件hello.txt
f = open("hello.txt","r")
# 读取文件内容赋值给变量c
c = f.read()
# 关闭文件
f.close()
# 输出c的值
print(c)