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
#xdata = []
#ydata = []
#zdata = []

#for j in range(len(delay[0])):
#    xdata.append(delay[year][j][1])
#    ydata
#    zdata.append(delay[year][j][3])
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
for i in range(len(xdata)):
    if int(str(delay[year][i]).strip('[')[:2]) in Aircraftgen:
        cmap.append('b')
#        temp = [delay[year][i][1],delay[year][i][2],delay[year][i][3]]
#        data1.append(temp)
        x1.append(delay[year][i][1])
        y1.append(delay[year][i][2])
        z1.append(delay[year][i][3])
#        cluster.append('aircraftgen')
    if int(str(delay[year][i]).strip('[')[:2]) in airframesystem:
        cmap.append('m')
#        temp = (delay[year][i][1],delay[year][i][2],delay[year][i][3])
#        data4.append(temp)
        x2.append(delay[year][i][1])
        y2.append(delay[year][i][2])
        z2.append(delay[year][i][3])
#        cluster.append('airframesystem')
    if int(str(delay[year][i]).strip('[')[:2]) in structure:
        cmap.append('g')
#        temp = (delay[year][i][1],delay[year][i][2],delay[year][i][3])
#        data4.append(temp)
        x3.append(delay[year][i][1])
        y3.append(delay[year][i][2])
        z3.append(delay[year][i][3])
#        cluster.append('structure')
    if int(str(delay[year][i]).strip('[')[:2]) in proprotor:
        cmap.append('r')
#        temp = (delay[year][i][1],delay[year][i][2],delay[year][i][3])
#        data4.append(temp)
        x4.append(delay[year][i][1])
        y4.append(delay[year][i][2])
        z4.append(delay[year][i][3])
#        cluster.append('proproter')
    if int(str(delay[year][i]).strip('[')[:2]) in powerplant:
        cmap.append('k')
#        temp = (delay[year][i][1],delay[year][i][2],delay[year][i][3])
#        data4.append(temp)
        x5.append(delay[year][i][1])
        y5.append(delay[year][i][2])
        z5.append(delay[year][i][3])
#        cluster.append('powerplant')
#    temp = []
data1 = (x1,y1,z1)
data2 = (x2,y2,z2)
data3 = (x3,y3,z3)
data4 = (x4,y4,z4)
data5 = (x5,y5,z5)
data = (data1,data2,data3,data4,data5)
colours = ('b', 'm', 'g', 'r', 'k')
groups = ('aircraft general','airframe systems','structure','propellor / rotor','powerplant')
#x, y, z = data
#ax.scatter3D(xdata, ydata, zdata, c = cmap, label = cluster)
#for data, color, group in zip(data, colors, groups):
#    x, y, z = data
#    ax.scatter(x, y, z, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
ax = fig.gca(projection='3d')


#blue_proxy = plt.Circle((0,0), 5,  fc = "b")
#pink_proxy = plt.Circle((0,0), 5,  fc = "m")
#green_proxy = plt.Circle((0,0), 5,  fc = "g")
#red_proxy = plt.Circle((0,0), 5,  fc = "r")
#black_proxy = plt.Circle((0,0), 5,  fc = "k")
#ax.set_xlim3d(0, 2000)
#ax.set_ylim3d(0,30)
#ax.set_zlim3d(0,30)
for data, color, group in zip(data, colours, groups):
    x, y, z = data
    ax.scatter(x, y, z, alpha=0.8, c=colours, edgecolors='none', s=30, label=group)

#ax.legend([blue_proxy,pink_proxy,green_proxy,red_proxy,black_proxy],['aircraft general','airframe systems','structure','propellor / rotor','powerplant'])
ax.set_xlabel('total delay')
ax.set_ylabel('delay frequency')
ax.set_zlabel('cancellation frequency')
plt.show

