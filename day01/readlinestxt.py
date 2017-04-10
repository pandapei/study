# -*- coding: UTF-8 -*-
# 以只读的方式打开文件hello.txt
f = open("hello.txt","r")
# 将文件所有内容赋值给c
c = f.readlines()
# 查看数据类型
print(type(c))
# 关闭文件
f.close()
# 遍历输出文件内容
for n in c:
    print(n)