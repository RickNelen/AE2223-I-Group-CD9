# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:15:10 2018

@author: Laurens
"""

import lib.core as core


k = core.unpickle("./Data.txt")
k = sorted(k,key=lambda x: x[5])

freqlist = []
i=0
c=0
while i <= len(k):
    if k[i,5] = k[i-1,5]:
        c += 1
        i += 1
    if k[i,5] != k[i-1,5]:
        freqlist.append(k[i-1,5],c)
        c = 0
        i+= 1