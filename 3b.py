#!/usr/bin/python
#-*- coding: utf-8 -*-
# 3题b小问
# 画出不同类型的年龄分布
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import math
from xlrd import open_workbook

#wb = open_workbook('/media/rongliangzi/新加卷/学习资料/研一/大数据分析/hw1/data.xlsx')
wb = open_workbook('/home/rongliangzi/PycharmProjects/BigDataAnalysisHW1/data.xlsx')
min_age = 0
max_age = 70
x_data=range(min_age,max_age,1)

worksheet = wb.sheet_by_index(0)
cols = worksheet.col_values(6)
cate = worksheet.col_values(1)
container = [([0] * (max_age-min_age)) for i in range(5)]
data_var = [0 for i in range(5)]

for i in range(1,len(cols)):
    container[int(cate[i])-1][int(math.floor(cols[i]))] += 1

array_container = np.array(container)

for i in range(5):
    plt.plot(x_data, container[i], 'o-', label=i, linewidth=1)
    data_var[i] = array_container[i].var()
    print (data_var[i])

plt.title(u"avrage age distribution in dif cate")
plt.legend()
plt.xlabel(u"avrage age")
plt.ylabel(u"number")

plt.show()
print 'over!'