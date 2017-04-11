# -*- coding: UTF-8 -*-
# 以只读的模式打开文件write.txt，没有则创建，有则覆盖内容
file = open("write.txt","w")
# 在文件内容中写入字符串test write
file.write("test write")
# 关闭文件
file.close()