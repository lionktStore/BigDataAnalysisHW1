#!/usr/bin/python
#-*- coding: utf-8 -*-
# 4题,选择col[2],col[3],col[10]画出图像，看是否满足(1)随机采样(2)同方差(3)残差正态分布
# 标注行定义了数据是否取对数
import matplotlib.pyplot as plt
import xlrd
import math
import numpy as np
from xlrd import open_workbook

col_sel = [2,3,10]
wb = open_workbook('/home/rongliangzi/PycharmProjects/BigDataAnalysisHW1/data.xlsx')
worksheet = wb.sheet_by_index(0)
x_data=[]
container = [[] for i in range(3)]
for i in range(3):
    cols = worksheet.col_values(col_sel[i])
    cols.pop(0)
    for j in range(len(cols)):
        container[i].append(cols[j])
y_data=[[] for i in range(3)]
cate = worksheet.col_values(1)

#draw the empirical pdf of each feature columns
plt.figure(12)
for i in range(3):
    ary_cols = np.array(container[i])
    min_num = int(math.floor(ary_cols.min()))
    max_num = int(math.ceil(ary_cols.max()))
    x_data=range(min_num,max_num+1)
    y_data=[0 for j in range(min_num,max_num+1)]

    for num in range(len(ary_cols)):
        index = int(math.floor(ary_cols[num]))-min_num
        if index<=max_num-min_num and index>=0:
            y_data[index]+=1
        else:
            print num
    plt.subplot(231+i)
    plt.plot(x_data, y_data, '-',label=i,linewidth=1)
    s_title = 'col[%d] raw data'%(col_sel[i])
    plt.title(s_title)

    ary_cols = np.log(ary_cols)
    min_num = int(math.floor(ary_cols.min()))
    max_num = int(math.ceil(ary_cols.max()))
    x_data = range(min_num, max_num + 1)
    y_data = [0 for j in range(min_num, max_num + 1)]
    for num in range(len(ary_cols)):
        index = int(math.floor(ary_cols[num])) - min_num
        if index <= max_num - min_num and index >= 0:
            y_data[index] += 1
        else:
            print num
    plt.subplot(234 + i)
    plt.plot(x_data, y_data, '-', label=i, linewidth=1)
    s_title = 'col[%d] log data'%(col_sel[i])
    plt.title(s_title)

#test the std of raw data and log data

for i in range(3):
    std = []

    cate_container = [[] for it in range(5)]
    for j in range(len(container[i])):
        cate_container[int(cate[j+1])-1].append(container[i][j])
    for k in range(5):
        std.append(np.std(np.array(cate_container[k])))
    print 'col[',col_sel[i],'] raw data std: ',std

#test the std of log data
for i in range(3):
    log_std = []
    cate_container = [[] for it in range(5)]
    for j in range(len(container[i])):
        cate_container[int(cate[j+1])-1].append(container[i][j])

    for k in range(5):
        log_cate_con = np.log(np.array(cate_container[k]))
        log_std.append(np.std(log_cate_con))
    print 'col[',col_sel[i],'] log data std: ',log_std

print 'over!'
plt.show()
