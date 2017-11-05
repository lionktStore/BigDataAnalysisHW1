#!/usr/bin/python
#-*- coding: utf-8 -*-
# 3题b小问
# 画出不同类型的年龄分布
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import math
from xlrd import open_workbook
from scipy.stats import normaltest

wb = open_workbook('/home/rongliangzi/PycharmProjects/BigDataAnalysisHW1/data.xlsx')
min_age = 0
max_age = 60
x_data=range(min_age,max_age,1)

worksheet = wb.sheet_by_index(0)
cols = worksheet.col_values(6)
cate = worksheet.col_values(1)
counter = [([0] * (max_age-min_age)) for i in range(5)]
data_var = [0 for i in range(5)]
container = [[]for i in range(5)]

for i in range(1,len(cols)):
    counter[int(cate[i])-1][int(math.floor(cols[i]))] += 1
for i in range(1,len(cols)):
    container[int(cate[i]-1)].append(cols[i])
array_container = np.array(container)

for i in range(5):
    plt.plot(x_data, counter[i], 'o-', label=i, linewidth=1)
    data_var[i] = np.std(array_container[i])
    print 'the std of ',i+1,' cate is ',data_var[i]

plt.title(u"avrage age distribution in dif cates")
plt.legend()
plt.xlabel(u"avrage age")
plt.ylabel(u"number")

for i in range(5):
    (s,p)=normaltest(container[i])
    if p > 0.05:
        print 'p = ',p,', p > 0.05, the data in ',i+1,' cate follows Gaussian Distribution'
    else:
        print 'p = ',p,', p < 0.05, the data in ',i+1,' cate does not follow Gaussian Distribution'

print 'over!'
plt.show()