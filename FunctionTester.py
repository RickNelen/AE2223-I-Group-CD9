#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:29:09 2018

@author: Misa
"""

import lib.core as core
import lib.numericals as numericals
import pickle
import time



with open("./Data.txt", "rb") as fp:   # Unpickling
   b = pickle.load(fp)
   
min = core.datetosec(1986,1,1)
max = core.datetosec(2017,1,1)

c = []

for i in range(len(b)):
    if b[i][2] > min and b[i][2] < max:
        c.append(b[i])
        


