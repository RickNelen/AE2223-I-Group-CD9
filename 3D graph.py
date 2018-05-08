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

xdata = []
ydata = []
zdata = []
#for i in range(len(delay)):
for j in range(len(delay[0])):
    xdata.append(delay[0][j][1])
    ydata.append(delay[0][j][2])
    zdata.append(delay[0][j][3])
ax = plt.axes(projection='3d')
cmap = []
for i in range(len(xdata)):
    
ax.scatter3D(xdata, ydata, zdata, cmap='Greens')
plt.show