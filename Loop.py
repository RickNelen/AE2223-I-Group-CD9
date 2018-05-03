#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 16:33:07 2018

@author: Misa
"""

import lib.core as core
import numpy as np
import lib.numericals as numericals

b = core.unpickle("./Data.txt")

h = core.getbyCancelled(b,0)

k = core.sortata(h,2)

flist = []
onlydata= []
c=1
l = []
l.append(k[0][3])
#
#for i in range(1,len(k)):
##for i in range(1,20000):
#    if k[i][5] == k[i-1][5]:
#        l.append(k[i][3])
#    if k[i][5] != k[i-1][5]:
#        j = []
#        j.append(k[i-1][5])
#        j.append(l)
#        flist.append(j)
#        onlydata.append(j[1])
#        cancel = k[i][4] 
#        l = []
#        l.append(k[i][3])
#        
#onlydata = [x for x in onlydata if len(x) > 50]


somedata = np.matrix([1,2,3,4,5,5,6,4,7]) + 15

# use the hiscalc to get the histograms
histograms = core.hiscalc(somedata)
#core.hisplot(histograms)
weibulls = numericals.fitweibull(histograms)



