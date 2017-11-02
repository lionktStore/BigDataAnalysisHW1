#!/usr/bin/python
#-*- coding: utf-8 -*-
import numpy as np
from scipy.stats import chi2
from scipy.stats import t
from scipy.stats import f
from scipy.stats import norm

# F distribution
alpha = 0.05
print f.isf(alpha, 5, 2000)