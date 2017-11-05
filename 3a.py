#!/usr/bin/python
#-*- coding: utf-8 -*-
# 3题a小问
# 画出平均年龄分布图像
import matplotlib.pyplot as plt
import xlrd
import math
import numpy as np
from xlrd import open_workbook
#读取数据
#wb = open_workbook('/media/rongliangzi/新加卷/学习资料/研一/大数据分析/hw1/data.xlsx')
wb = open_workbook('/home/rongliangzi/PycharmProjects/BigDataAnalysisHW1/data.xlsx')
worksheet = wb.sheet_by_index(0)
cols = worksheet.col_values(6);
cols.pop(0)
ary_cols = np.array(cols)
min_age = int(math.floor(ary_cols.min()))
max_age = int(math.ceil(ary_cols.max()))

x_data=range(min_age,max_age+1)
y_data=[0 for i in range(min_age,max_age+1)]

#delete the first row which represents name
for num in range(0,len(ary_cols)):
    y_data[int(math.floor(ary_cols[num]))-min_age]+=1
plt.plot(x_data, y_data, 'ro-',linewidth=1)
plt.title(u"avrage age distribution")
plt.legend()

plt.xlabel(u"avrage age")
plt.ylabel(u"number")


plt.show()
print 'over!'
