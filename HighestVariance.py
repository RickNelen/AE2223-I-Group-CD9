# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 08:22:57 2018

@author: Till
"""
import numpy as np
import lib.core as core
import lib.numericals as numericals
import pickle
import matplotlib.pyplot as plt


def weibull(beta, x):
        return beta[0]/beta[1] * np.power((x/beta[1]),(beta[0]-1)) * np.exp(-1* np.power((x/beta[1]),beta[0]))
    

with open("./Data.txt", "rb") as fp:   # Unpickling list all types
   b = pickle.load(fp)
   


actype = 1 # define this
atalevel = 2 # 2 means chapter. higher number means more detailed ata level
timeframe = [2000,2003]

b = core.getbyType(b,actype) # filter by type
b = core.getbyDate(b, timeframe)
b = core.getbyCancelled(b, 0)



# main loop, probably takes forever
ata = []
data = []
means = []
variances = []
histos = []

for atanum in range(1,10**atalevel): # 1 to 99 in steps of 1
    atastr = str(atanum)
    while len(atastr) < atalevel:
        atastr = '0'+atastr
    filtered = core.getbyATA(b,atastr)
    if len(filtered):
        ata.append(atastr)
        data.append(filtered)

histos = core.hiscalc(b,ata,len(ata)*[actype],len(ata)*[timeframe],600)
weibulls = numericals.fitweibull(histos)

means     = weibulls[1]
variances = weibulls[2]

filterSET = []
filterATA = [] 
for i in range(len(weibulls[0])):
    if weibulls[1][i] * weibulls[2][i] * weibulls[0][i][1]:
        temp = []
        for j in range(len(weibulls)):
            temp.append(weibulls[j][i]) # small hack to always get all elements of the weibulls array
        
        filterATA.append(ata[i])
        filterSET.append(temp)
        xvals = range(200)
        plt.close()
        plt.plot(xvals, weibull(weibulls[0][i], xvals))
        plt.show()

filterSET = np.array(filterSET)

plt.figure(1)
plt.hist(np.concatenate(filterSET[:,1]))

plt.figure(2)
plt.hist(np.concatenate(filterSET[:,2]))


plt.show





