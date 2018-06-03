# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:11:08 2018

@author: Till
"""

# stats test
import numpy as np
from numpy import random as rd
from matplotlib import pyplot as plt

n = 50 # number of samplings
k = 50 # number of samples per sampling
par = 1.5

means = np.zeros([n, 1])
conti = np.zeros([k, 1])
for i in range(n):
    conti = conti + (rd.exponential(1/par,k))
    means[i] = np.mean(rd.exponential(1/par,k))

plt.hist( (means).T[0], density=True)
plt.hist( np.concatenate(conti)/n, density=True )
plt.hist( rd.gamma(k, 1/par, n)/k ,density=True)
plt.show()
