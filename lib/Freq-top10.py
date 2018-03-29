# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:15:10 2018

@author: Laurens
"""

import core as core


k = core.unpickle("../Data.txt")
k = core.sortata(k,2)

freqlist = []
i=0
c=0
for i in range(1,len(k)):
    if k[i][5] == k[i-1][5]:
        c += 1
    if k[i][5] != k[i-1][5]:
        j = []
        j.append(k[i-1][5])
        j.append(c)
        freqlist.append(j)
        c = 0
    if k[i-1][5] != k[i-2][5]:
        c = 1
        j = []
        j.append(k[i-1][5])
        j.append(c)
        c = 0
        
freqlist = sorted(freqlist,key=lambda x: x[1] ,reverse=True)