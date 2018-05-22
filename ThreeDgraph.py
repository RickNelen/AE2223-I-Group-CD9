# -*- coding: utf-8 -*-
"""
Created on Thu May 03 10:24:26 2018

@author: Laurens
"""
import lib.core as core
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


k = core.unpickle("./Data.txt")                                                 #getting the data ready
k = core.sortata(k, 4)
delay, date = core.getdelaylist([1988,2015],36,k)                               #getting the data ready till here




for i in range(len(delay)):                                                  #removing all the 0 delays.
    delay[i] = [x for x in delay[i] if x[-1] != 0]


for year in range(len(delay)):
    #DON"T FUCKING CHANGE ANYTHING
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
    Aircraftgen = [0,1,2,3,4,5,6,7,8,9,10,11,12,14,18] #->blue
    airframesystem = [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50] #-> pink
    structure = [51,52,53,54,55,56,57] #-> orange
    proprotor = [60,61,62,63,64,65,66,67] #-> red
    powerplant = [70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85.91,92] #-> black
    cluster = ['Aircraftgen', 'airframesystem', 'structure', 'proprotor', 'powerplant']
    for i in range(len(delay[year])):
        if int(str(delay[year][i]).strip('[')[:2]) in Aircraftgen:
            cmap.append('b')
            x1.append(delay[year][i][1])
            y1.append(delay[year][i][2])
            z1.append(delay[year][i][3])
        if int(str(delay[year][i]).strip('[')[:2]) in airframesystem:
            cmap.append('m')
            x2.append(delay[year][i][1])
            y2.append(delay[year][i][2])
            z2.append(delay[year][i][3])
        if int(str(delay[year][i]).strip('[')[:2]) in structure:
            cmap.append('g')
            x3.append(delay[year][i][1])
            y3.append(delay[year][i][2])
            z3.append(delay[year][i][3])
        if int(str(delay[year][i]).strip('[')[:2]) in proprotor:
            cmap.append('r')
            x4.append(delay[year][i][1])
            y4.append(delay[year][i][2])
            z4.append(delay[year][i][3])
        if int(str(delay[year][i]).strip('[')[:2]) in powerplant:
            cmap.append('k')      
            x5.append(delay[year][i][1])
            y5.append(delay[year][i][2])
            z5.append(delay[year][i][3])
    
    data1 = (np.asarray(x1),np.asarray(y1),np.asarray(z1))
    data2 = (np.asarray(x2),np.asarray(y2),np.asarray(z2))
    data3 = (np.asarray(x3),np.asarray(y3),np.asarray(z3))
    data4 = (np.asarray(x4),np.asarray(y4),np.asarray(z4))
    data5 = (np.asarray(x5),np.asarray(y5),np.asarray(z5))
    data = (data1,data2,data3,data4,data5)
    colors = ('b', 'm', 'g', 'r', 'k')
    groups = ('aircraft general','airframe systems','structure','propellor / rotor','powerplant')
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
    ax = fig.gca(projection='3d')
     
    for datainst, color, group in zip(data, colors, groups):
        x, y, z = datainst
        ax.scatter(x, y, z, alpha=0.65, c=color, s=10, label=group)
    
    ax.set_xlim(0,20000)
    #ax.set_ylim(0,30)
    #ax.set_zlim(0,30)
    ax.set_xlabel('total delay')
    ax.set_ylabel('delay frequency')
    ax.set_zlabel('cancellation frequency')
    plt.title('3D scatterplot period '+ str(year+1))
    plt.legend(loc=2)
    plt.show()

