# -*- coding: utf-8 -*-
name = raw_input('input username')
if name == "mark":
    print "超级管理员"
elif name == "tom":
    print "普通管理员"
elif name == "tony" or name == "rain":
    print "业务主管"
else:
    print "普通用户"