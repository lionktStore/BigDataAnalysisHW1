#!/usr/bin/python
#-*- coding: utf-8 -*-
# 4题,选择col[2],col[3],col[10]画出图像，看是否满足
# 第21行定义了数据是否取对数
import matplotlib.pyplot as plt
import xlrd
import math
import numpy as np
from xlrd import open_workbook

col_sel = [2,3,10]
#wb = open_workbook('/media/rongliangzi/新加卷/学习资料/研一/大数据分析/hw1/data.xlsx')
wb = open_workbook('/home/rongliangzi/PycharmProjects/BigDataAnalysisHW1/data.xlsx')
worksheet = wb.sheet_by_index(0)
x_data=[]
y_data=[]
for i in col_sel:
    cols = worksheet.col_values(i);
    col_name = cols[0]
    cols.pop(0)
    ary_cols = np.array(cols)
    #ary_cols = np.log(ary_cols)
    min_num = int(math.floor(ary_cols.min()))
    max_num = int(math.ceil(ary_cols.max()))
    x_data=range(min_num,max_num+1)
    y_data=[0 for j in range(min_num,max_num+1)]

    for num in range(len(ary_cols)):
        index = int(math.floor(ary_cols[num]))-min_num
        if index<max_num-min_num and index>=0:
            y_data[index]+=1
        else:
            print num
    plt.plot(x_data, y_data, '-',label=i,linewidth=1)
    plt.title(u"data distribution")
    plt.legend()

    plt.xlabel(u"data")
    plt.ylabel(u"number")

plt.show()
print 'over!'