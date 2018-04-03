# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:11:08 2018

@author: Till
"""

# stats test

import numpy as np
from numpy import random as rd
from matplotlib import pyplot as plt

n = 1000 # number of samplings
k = 10000 # number of samples per sampling
par = 1.5

means = np.zeros([n, 1])
for i in range(n):
    means[i] = np.mean(rd.exponential(1/par,k))

print (means).T
print rd.gamma(k, 1/par, n)/k

