# -*- coding: utf-8 -*-
"""
Created on Tue May 08 16:12:29 2018

@author: Laurens
"""

import lib.core as core
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
mpl.rcParams['legend.fontsize'] = 10

k = core.unpickle("./Data.txt")                                                 #getting the data ready
k = core.sortata(k, 2)
delay, date = core.getdelaylist([1988,2015],36,k)                               #getting the data ready till here

for i in range(len(delay)):                                                     #removing all the 0 delays.
    delay[i] = [x for x in delay[i] if x[-1] != 0]
    
top_first_year = []
main = []
amounttopnumbers = 3
l = []
temp = []
#l =[[]]*amounttopnumbers
s = 0
i = 0

while i < amounttopnumbers:
#    if int(str(delay[0][i][0])[:2]) in top_first_year:
#        s +=1
#    else:
#        top_first_year.append(int(str(delay[0][(i+s)][0])[:2]))
#        i += 1
    top_first_year.append(delay[0][i][0])
    i += 1



for i in range(len(delay)):
    for j in range(len(delay[i])):
        if int(str(delay[i][j][0])[:2]) in top_first_year:
            main.append(delay[i][j])
main.sort(key= lambda x:x[0], reverse = True)

for i in range(len(top_first_year)):
    for j in range(len(main)):
        if main[j][0] == top_first_year[i]:
            temp.append(main[j])
    l.append(temp)
    temp = []
    
x1 = []
x2 = []
x3 = []
y1 = []
y2 = []
y3 = []
z1 = []
z2 = []
z3 = []

for i in range(len(l[0])):
    x1.append(l[0][i][1])
    x2.append(l[1][i][1])
    x3.append(l[2][i][1])
    y1.append(l[0][i][2])
    y2.append(l[1][i][2])
    y3.append(l[2][i][2])
    z1.append(l[0][i][3])
    z2.append(l[1][i][3])
    z3.append(l[2][i][3])
x1 = np.float64(np.asarray(x1))
x2 = np.float64(np.asarray(x2))
x3 = np.float64(np.asarray(x3))
y1 = np.float64(np.asarray(y1))
y2 = np.float64(np.asarray(y2))
y3 = np.float64(np.asarray(y3))
z1 = np.float64(np.asarray(z1))
z2 = np.float64(np.asarray(z2))
z3 = np.float64(np.asarray(z3))


ax.plot(x1,y1,z1, color = 'black', label = 'ATA ' +str(l[0][0][0]))
ax.plot(x2,y2,z2, color = 'red', label = 'ATA ' +str(l[1][0][0]))
ax.plot(x3,y3,z3, color = 'green', label = 'ATA ' +str(l[2][0][0]))
ax.set_xlabel('total delay')
ax.set_ylabel('delay frequency')
ax.set_zlabel('cancellation frequency')
ax.legend()
plt.show
    