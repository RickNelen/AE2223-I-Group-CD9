# -*- coding: utf-8 -*-
"""
Created on Thu May 03 10:24:26 2018

@author: Laurens
"""
import lib.core as core
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

k = core.unpickle("./Data.txt")                                                 #getting the data ready
k = core.sortata(k, 4)
delay, date = core.getdelaylist([1988,2015],36,k)                               #getting the data ready till here

for i in range(len(delay)):                                                  #removing all the 0 delays.
    delay[i] = [x for x in delay[i] if x[-1] != 0]
year = 0
xdata = []
ydata = []
zdata = []
#for i in range(len(delay)):
for j in range(len(delay[0])):
    xdata.append(delay[year][j][1])
    ydata.append(delay[year][j][2])
    zdata.append(delay[year][j][3])
ax = plt.axes(projection='3d')
cmap = []
Aircraftgen = [0,1,2,3,4,5,6,7,8,9,10,11,12,14,18] #->blue
airframesystem = [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50] #-> pink
structure = [51,52,53,54,55,56,57] #-> orange
proprotor = [60,61,62,63,64,65,66,67] #-> red
powerplant = [70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85.91,92] #-> black

for i in range(len(xdata)):
    if int(str(delay[year][i]).strip('[')[:2]) in Aircraftgen:
        cmap.append('b')
    if int(str(delay[year][i]).strip('[')[:2]) in airframesystem:
        cmap.append('m')
    if int(str(delay[year][i]).strip('[')[:2]) in structure:
        cmap.append('g')
    if int(str(delay[year][i]).strip('[')[:2]) in proprotor:
        cmap.append('r')
    if int(str(delay[year][i]).strip('[')[:2]) in powerplant:
        cmap.append('k')
    
ax.scatter3D(xdata, ydata, zdata, c = cmap)
plt.show

#ax.scatter3D(xdata, ydata, zdata, c = cmap)
#ax.set_xlim3d(0, 2000)
#ax.set_ylim3d(0,30)
#ax.set_zlim3d(0,30)
#plt.show