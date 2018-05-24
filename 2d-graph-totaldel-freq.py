# -*- coding: utf-8 -*-
"""
Created on Fri May 18 15:59:34 2018

@author: Laurens
"""
import lib.core as core
import matplotlib.pyplot as plt
import numpy as np


k = core.unpickle("./Data.txt")                                                 #getting the data ready
k = core.sortata(k, 4)
delay, date = core.getdelaylist([1988,2015],36,k)                               #getting the data ready till here




for i in range(len(delay)):                                                     #removing all the 0 delays.
    delay[i] = [x for x in delay[i] if x[2] != 0]

cmap = []
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
z1 = []
z2 = []
z3 = []
z4 = []
z5 = []
for year in range(len(delay)):
    Aircraftgen = [0,1,2,3,4,5,6,7,8,9,10,11,12,14,18] #->blue
    airframesystem = [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50] #-> pink
    structure = [51,52,53,54,55,56,57] #-> orange
    proprotor = [60,61,62,63,64,65,66,67] #-> red
    powerplant = [70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85.91,92] #-> black
    cluster = ['Aircraftgen', 'airframesystem', 'structure', 'proprotor', 'powerplant']    
    for i in range(len(delay[year])):
        if delay[year][i][1] < 200000:
            if int(str(delay[year][i]).strip('[')[:2]) in Aircraftgen:
                cmap.append('b')
                x1.append(delay[year][i][1])#/delay[year][i][2])
                y1.append(delay[year][i][2])
                z1.append(delay[year][i][3])#/float(delay[year][i][3]+delay[year][i][2]))
            if int(str(delay[year][i]).strip('[')[:2]) in airframesystem:
                cmap.append('m')
                x2.append(delay[year][i][1])#/delay[year][i][2])
                y2.append(delay[year][i][2])
                z2.append(delay[year][i][3])#/float(delay[year][i][3]+delay[year][i][2]))
            if int(str(delay[year][i]).strip('[')[:2]) in structure:
                cmap.append('g')
                x3.append(delay[year][i][1])#/delay[year][i][2])
                y3.append(delay[year][i][2])
                z3.append(delay[year][i][3])#/float(delay[year][i][3]+delay[year][i][2]))
            if int(str(delay[year][i]).strip('[')[:2]) in proprotor:
                cmap.append('r')
                x4.append(delay[year][i][1])#/delay[year][i][2])
                y4.append(delay[year][i][2])
                z4.append(delay[year][i][3])#/float(delay[year][i][3]+delay[year][i][2]))
            if int(str(delay[year][i]).strip('[')[:2]) in powerplant:
                cmap.append('k')      
                x5.append(delay[year][i][1])#/delay[year][i][2])
                y5.append(delay[year][i][2])
                z5.append(delay[year][i][3])#/float(delay[year][i][3]+delay[year][i][2]))
colors = ('b', 'm', 'g', 'r', 'k')
#    linlsqx = np.asarray(x1 + x2 + x3 + x4 +x5)# + np.asarray(x2) + np.asarray(x3) + np.asarray(x4) + np.asarray(x5)
#    linlsqy = np.asarray(y1 + y2 + y3 + y4 +y5)# + np.asarray(y2) + np.asarray(y3) + np.asarray(y4) + np.asarray(y5)
groups = ('aircraft general','airframe systems','structure','propellor / rotor','powerplant')
x = [x1,x2,x3,x4,x5]
y = [y1,y2,y3,y4,y5]
for i in range(5):
    plt.scatter(y[i], x[i], alpha=0.65, c=colors[i], s=10, label=groups[i])
xtot = x1+x2+x3+x4+x5
ytot = y1+y2+y3+y4+y5
xtot = np.asarray(xtot)
ytot = np.asarray(ytot)
zz = np.polyfit(xtot, ytot, 1)
zz = list(zz)
zz[0] = float(zz[0])
zz[1] = float(zz[1])
lsty = [zz[:-1],(max(xtot)*zz[0]+zz[:-1])]
lstx = [0,max(xtot)]
label1 = str(round(zz[0],3)) + 'x +' + str(round(zz[1],2))
plt.plot(lsty,lstx, c = 'black', label = label1)
plt.title('Correlation between total delay and delay frequency')
plt.xlabel('Total delay')
plt.ylabel('Delay frequency')
plt.legend()
plt.show