# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 19:17:20 2018

@author: Till
"""

# provides an estimate of the fleetsize in 1 year increments

import numpy as np
import lib.core as core
import pickle
import matplotlib.pyplot as plt

with open("./Data.txt", "rb") as fp:   # Unpickling list all types
   b = pickle.load(fp)

years   = range(2011,2015)
actypes = range(1,4)

totalacs   = [] # all acs in the year and type range
acdatabase = {} # for every year there's a dict of the three types and for each type there is a dict of the serial numbers
for year in years:
    currentyear = {}
    c = core.getbyDate(b, [year,year+1])
    for actype in actypes:
        currentactype = []
        d = core.getbyType(c,actype)
        for entry in d:
            if entry[0] not in totalacs:
                totalacs.append(entry[0])
            if entry[0] not in currentactype:
                currentactype.append(entry[0])
        currentyear[str(actype)] = (currentactype)
    acdatabase[str(year)] = currentyear

typenums = []
for actype in actypes:
    curtype = []
    for year in years:
        curtype.append(len(acdatabase[str(year)][str(actype)]))
    typenums.append(curtype)



#plt.plot(years,typenums[0], label='Type 1')
#plt.plot(years,typenums[1], label='Type 2')
#plt.plot(years,typenums[2], label='Type 3')
#plt.legend()
#plt.savefig("fleetsize.eps")
