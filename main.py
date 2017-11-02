#!/usr/bin/python
#-*- coding: utf-8 -*-
#画出平均年龄分布图像
import matplotlib.pyplot as plt
import xlrd
import math
from xlrd import open_workbook

min_age = 0
max_age = 70
x_data=range(min_age,max_age,1)
y_data=[0 for i in range(min_age,max_age)]

wb = open_workbook('/media/rongliangzi/新加卷/学习资料/研一/大数据分析/hw1/data.xlsx')


worksheet = wb.sheet_by_index(0)
cols = worksheet.col_values(6);
for num in range(1,len(cols)):
    y_data[int(math.floor(cols[num]))]+=1
plt.plot(x_data, y_data, 'ro-',linewidth=1)
plt.title(u"avrage age distribution")
plt.legend()

plt.xlabel(u"avrage age")
plt.ylabel(u"number")


plt.show()
print 'over!'
