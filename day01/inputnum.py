#!/use/bin/env python
# _*_ coding:utf-8 _*_
# 只需脚本是让用户输入一个数字，并把值赋值给变量n
n = int(input("Pless Numbers: "))
# 如果n大于10
if n > 10:
    # 输出n > 10
    print("n > 10")
# 如果n等于10
elif n == 10:
    # 输出n == 10
    print("n == 10")
# 否则
else:
    # 输出n < 10
    print("n < 10")