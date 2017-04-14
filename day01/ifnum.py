#_*_coding:utf-8_*_
num = [11,22,33,44,55,66,77,88,99,90]
dict = {
    'k1':[],
    'k2':[]
}
for n in range(len(num)):
    if num[n] <= 66:
        dict['k1'].append(num[n])
    else:
        dict['k2'].append(num[n])
print(dict.get("k1"))
print(dict.get("k2"))