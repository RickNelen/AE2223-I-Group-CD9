# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:45:03 2018

@author: Laurens
"""

import core as core


k = core.unpickle("../Data.txt")
k = core.sortata(k,2)

freqlist = []
i=0
c=0
h = []
for i in range(1,len(k)):
    
    if k[i][5] == k[i-1][5]:
        c += k[i][3]
        h.append(k[i][3])
    if k[i][5] != k[i-1][5]:
        j = []
        j.append(k[i-1][5])
        j.append(c)
        freqlist.append(j)
        c = 0
        h = []
        
freqlist = sorted(freqlist,key=lambda x: x[1] ,reverse=True)