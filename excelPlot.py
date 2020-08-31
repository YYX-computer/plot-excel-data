# magic remark
# -*- encoding:utf-8 -*-
import xlrd
import matplotlib.pyplot as plt
import os
fig = plt.figure()
while(1):
    name = input('请输入文件名:')
    if(not os.path.exists(name)):
        print('文件不存在')
        continue
    _,ext = os.path.splitext(name)
    if(ext != '.xlsx'):
        print('错误的文件格式')
        continue
    break
book = xlrd.open_workbook(name)
sheets = book.sheets()
subs = []
while(1):
    flag = True
    val = input('请输入排版格式(x,y):')
    try:
        xy = val.split(',')
        x,y = [int(xy[0]),int(xy[1])]
        if(x * y != len(sheets)):
            print('错误的格式')
            flag = False
    except Exception as e:
        print(f'错误的格式:{e}')
        flag = False
    if(flag):
        break
for i in range(len(sheets)):
    sub = fig.add_subplot(x,y,i + 1)
    subs.append(sub)
for i in range(len(sheets)):
    p = subs[i]
    s = sheets[i]
    f = 1
    x,y = [],[]
    if(type(s.row_values(0)[0]) != str and type(s.row_values(0)[1]) != str):
        f = 0
    for j in range(f,s.nrows):
        r = s.row_values(j)
        x.append(r[0])
        y.append(r[1])
    p.plot(x,y)
plt.show()