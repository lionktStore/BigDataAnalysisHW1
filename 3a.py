#!/usr/bin/python
#-*- coding: utf-8 -*-
# 3题a小问
# 画出平均年龄分布图像
import matplotlib.pyplot as plt
import xlrd
import math
import numpy as np
from xlrd import open_workbook
from scipy.stats import normaltest

#读取数据
wb = open_workbook('/home/rongliangzi/PycharmProjects/BigDataAnalysisHW1/data.xlsx')
worksheet = wb.sheet_by_index(0)
cols = worksheet.col_values(6);
#delete the first row which represents name
cols.pop(0)
ary_cols = np.array(cols)
min_age = int(math.floor(ary_cols.min()))
max_age = int(math.ceil(ary_cols.max()))

x_data=range(min_age,max_age+1)
y_data=[0 for i in range(min_age,max_age+1)]

for num in range(0,len(ary_cols)):
    y_data[int(math.floor(ary_cols[num]))-min_age] += 1
plt.plot(x_data, y_data, 'ro-',label=u"age",linewidth=1)
plt.title(u"avrage age distribution")
plt.legend()

plt.xlabel(u"avrage age")
plt.ylabel(u"number")
plt.show()
#close the plot and the result will show
#use the normaltest to test if the data follow Gaussian Distribution
(s,p)=normaltest(y_data)
if p > 0.05:
    print 'p=',p,', p > 0.05, the data follows Gaussian Distribution'
print 'over!'
