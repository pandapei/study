#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 定义一个拥有省市县的字典
dic = {
    u"河北": {
        u"石家庄": ["鹿泉", "藁城", "元氏"],
        u"邯郸": ["永年", "涉县", "磁县"],
    },
    u"河南": {
        u"郑州市":["中原区","二七区","金水区"],
        u"洛阳市":["涧西区","西工区","老城区"]
    },
    u"山西": {
        u"太原市":["迎泽区","杏花岭区","万柏林区"],
        u"大同市":["大同县","天镇县","浑源县"]
    }
}
# 控制while循环的开关
switch = "on"
# 执行脚本就显示已经进入中国
print(u"\n你已进入中国\n")
# 开始执行while循环
while switch == "on":
    # 省得列表
    sheng = []
    # 市的列表
    shi = []
    # 镇的列表
    zhen = []
    # 让用户选择进入的生
    while switch == "on":
        # 输出省得列表
        for sheng_n, sheng_v in enumerate(dic, 1):
            print(sheng_n, sheng_v)
            sheng.append(sheng_v)
        # 用户输出选择进入的省
        try:
            # 用户输入的必须为整数
            sheng_inp = int(input("请选择你要进入的城市序列："))
        except ValueError:
            # 如果不是整数就报错然后让用户重新输入
            print("序列输入错误，请重新输入")
            continue
        # 如果用户输入的证书是0或者大于列表的序列就让用户重新输入
        if sheng_inp > sheng_n or sheng_inp == 0:
            print("序列输入错误，请重新输入")
            continue
        # 输入正确之后输出用户当前在哪里
        print("\n你已进入中国--->", sheng[sheng_inp - 1], "\n")
        # 选项
        while True:
            # 输出选项
            ify = input("b 返回上一级\nn 继续\nq 退出\n请输入你的选择：")
            # 如果用户输入的是指定的字母就退出当前循环
            if ify == "q" or ify == "b" or ify == "n":
                break
            # 如果不是指定字母就让用户重新输入
            else:
                print("输入错误，请重新输入！")
                continue
        # 如果用户输入的是b就返回上一级
        if ify == "b":
            continue
        # 如果用户输入的是q那么就把变量switch值改为off
        elif ify == "q":
            switch = "off"
            continue
        # 如果用户输入的是n就继续让用户选择市，注释就写到这儿把，下面的代码就相当于让用户重新选择省，只不过省改为市了
        while switch == "on":
            for shi_n, shi_v in enumerate(dic[sheng[sheng_inp - 1]], 1):
                print(shi_n, shi_v)
                shi.append(shi_v)
            try:
                shi_inp = int(input("请选择你要进入的城市序列："))
            except ValueError:
                print("序列输入错误，请重新输入")
                continue
            if shi_n < shi_inp or shi_inp == 0:
                print("序列输入错误，请重新输入")
                continue
            print("\n你已进入中国--->", sheng[sheng_inp - 1], "--->",shi[shi_inp - 1])
            while True:
                ify = input("b 返回上一级\nn 继续\nq 退出\n请输入你的选择：")
                if ify == "q" or ify == "b" or ify == "n":
                    break
                else:
                    print("输入错误，请重新输入！")
                    continue
            if ify == "b":
                continue
            elif ify == "q":
                switch = "off"
                continue
            while switch == "on":
                for zhen_n, zhen_v in enumerate(dic[sheng[sheng_inp - 1]][shi[shi_inp - 1]], 1):
                    print(zhen_n, zhen_v)
                    zhen.append(zhen_v)
                try:
                    zhen_inp = int(input("请选择你要进入的城市序列："))
                except ValueError:
                    print("序列输入错误，请重新输入")
                    continue
                if zhen_n < zhen_inp or zhen_inp == 0:
                    print("序列输入错误，请重新输入")
                    continue
                print("\n你已进入中国--->", sheng[sheng_inp - 1], "--->", shi[shi_inp - 1],"--->",zhen[zhen_inp - 1])
                while True:
                    ify = input("b 返回上一级\nn 继续\nq 退出\n请输入你的选择：")
                    if ify == "q" or ify == "b" or ify == "n":
                        break
                    else:
                        print("输入错误，请重新输入！")
                        continue
                if ify == "b":
                    continue
                elif ify == "q":
                    switch = "off"
                    continue