# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:23:38 2018

@author: Till
"""

import numpy as np
#from ThreeDgraph import output
#import random
import lib.core as core
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#k = core.unpickle("./Data.txt")                                                 #getting the data ready
#k = core.sortata(k, 4)
#delay, date = core.getdelaylist([1988,2015],36,k)                               #getting the data ready till here
#output = core.ThreeDgraph(delay, 3, 0)

columns = [[], [], []]
for line in output:
    columns[0].append(line[0])
    columns[1].append(line[1])
    columns[2].append(line[2])
    
data = np.array(columns)

#i = 10
#randset = []
#
#for k in range(i):
#    temp = np.matrix([random.random(), random.random(), random.random()])
#    temp = temp * np.matrix([[5.],[3.],[0.]]) + np.matrix([[1.],[1.],[1.]])
#    randset.append(temp)
#    
#data = np.array(randset)
#data = output[3]

covmat = np.cov(data)
eigvals, eigvecs = np.linalg.eig(covmat)
scaling = np.sqrt(eigvals)

mpoint = np.mean(data, axis=1)
uniformscale = 5
scalevec0 = mpoint + scaling[0]*eigvecs[:,0]*uniformscale
scalevec1 = mpoint + scaling[1]*eigvecs[:,1]*uniformscale
scalevec2 = mpoint + scaling[2]*eigvecs[:,2]*uniformscale


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot([mpoint[0],scalevec0[0]], [mpoint[1],scalevec0[1]],[mpoint[2],scalevec0[2]])
ax.plot([mpoint[0],scalevec1[0]], [mpoint[1],scalevec1[1]],[mpoint[2],scalevec1[2]])
ax.plot([mpoint[0],scalevec2[0]], [mpoint[1],scalevec2[1]],[mpoint[2],scalevec2[2]])
x,y,z = data
ax.scatter(x, y, z, alpha=0.65, c="k", s=2, label="test")