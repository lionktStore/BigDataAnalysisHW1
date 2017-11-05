#!/usr/bin/python
#-*- coding: utf-8 -*-
#col[2][3][10]做对数变换满足方差齐性后做ANOVA

import numpy as np
import xlrd
import math
import scipy
from scipy.stats import f

from xlrd import open_workbook
#read file
wb = open_workbook('/home/rongliangzi/PycharmProjects/BigDataAnalysisHW1/data.xlsx')
worksheet = wb.sheet_by_index(0)

cates = 5;
cate = worksheet.col_values(1)
cate.pop(0)
col_sel = [2,3,10]
cols = []
for i in range(3):
    cols = worksheet.col_values(col_sel[i])
    cols.pop(0)
    #做对数变换
    cols = np.log(np.array(cols))
    ary_mtx = [[] for it in range(cates)]
    for j in range(0,len(cols)):
        ary_mtx[int(cate[j])-1].append(int(math.floor(cols[j])))
    data_avr = [0 for i in range(cates)]
    data_std = [0 for i in range(cates)]
    for i in range(cates):
        npary = np.array(ary_mtx[i])
        data_avr[i] = npary.mean()
        data_std[i] = npary.std()
    alldata_avr = np.array(data_avr).mean()
    #cal the matrix ssb ssw dfb dfw msb msw f=msb/msw p
    ssb = 0
    ssw = 0
    avr = data_avr
    #ssb = np.sum(np.square(avr-alldata_avr))
    for i in range(cates):
        ssb += len(ary_mtx[i])*(data_avr[i]-alldata_avr)**2
        for j in range(len(ary_mtx[i])):
           ssw += (ary_mtx[i][j]-data_avr[i])**2
    dfb = cates-1
    dfw = len(cols)-cates
    msb = ssb/dfb
    msw = ssw/dfw
    F = msb/msw
    print 'col[',i,'] ANOVA result:'
    print ssb," ",dfb," ",msb," ",F
    print ssw,' ',dfw,' ',msw
    print ssb+ssw,' ',dfb+dfw
    #F(dfb,dfw) 带入求得f,与显著性阈值0.05比较
    a = 0.05
    x=f.isf(a,dfb,dfw)
    if F>x:
        print F,' ',x,'reject H0:The means of all groups are equal.'
    else:
        print F,' ',x,'not reject H0:The means of all groups are equal.'

print 'over'