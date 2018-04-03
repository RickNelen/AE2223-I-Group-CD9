#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 16:33:07 2018

@author: Misa
"""

import lib.core as core

b = core.unpickle("./Data.txt")

h = core.getbyCancelled(b,0)

k = core.sortata(h,2)

flist = []
c=1
l = []
l.append(k[0][3])

for i in range(1,len(k)):
    if k[i][5] == k[i-1][5]:
        l.append(k[i][3])
    if k[i][5] != k[i-1][5]:
        j = []
        j.append(k[i-1][5])
        j.append(l)
        flist.append(j)
        cancel = k[i][4] 
        l = []
        l.append(k[i][3])
