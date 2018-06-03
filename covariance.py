# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:23:38 2018

@author: Till
"""

import numpy as np
import lib.core as core
import lib.numericals as nums
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

k = core.unpickle("./Data.txt")                                                 #getting the data ready
k = core.sortata(k, 4)
delay, date = core.getdelaylist([1988,2015],36,k)                               #getting the data ready till here
output = core.ThreeDgraph(delay, range(len(delay)), 0)

columns = [[], [], []]
for line in output:
    if line[1] > 0: # can be used for filtering
        columns[0].append(line[0])
        columns[1].append(line[1])
        columns[2].append(line[2])
    
data = np.array(columns)
data = data.astype(float)
data_norm = np.zeros_like(data)
data_norm = data.astype(float)
data_norm[0] = data[0] / float(max(data[0]))
data_norm[1] = data[1] / float(max(data[1]))
data_norm[2] = data[2] / float(max(data[2]))



# simple 2d analysis

# compute fit
nums.polynomial_fit(data[0], data[1], 1, 1)

# 3d cov dim reduc analysis
covmat = np.cov(data_norm)   # get covariance matrix
eigvals, eigvecs = np.linalg.eig(covmat) # get eigenstuff
scaling = np.sqrt(eigvals) # get scaling factors

mpoint = np.mean(data_norm, axis=1) # get centre point
uniformscale = 5 # just some userdefined scaling factor
scalevec0 = mpoint + scaling[0]*eigvecs[:,0]*uniformscale*np.sign(eigvecs[0,0])
scalevec1 = mpoint + scaling[1]*eigvecs[:,1]*uniformscale*np.sign(eigvecs[0,1])
scalevec2 = mpoint + scaling[2]*eigvecs[:,2]*uniformscale*np.sign(eigvecs[0,2])




b = np.array([0,1,2])
maxevs=b[np.invert(abs(eigvals)==min(abs(eigvals)))]


# plotting

# level lines
fig2 = plt.figure()
ax = fig2.add_subplot(111)
for z in np.linspace(0,max(data_norm[2]),5):
    P2, N2, check2 = nums.plane_plane_intersect(np.array([0., 0., 1.]), np.array([0., 0., float(z)]), np.cross(eigvecs[:,maxevs[0]],eigvecs[:,maxevs[1]]), mpoint)
    a = N2[1]/N2[0]
    b = P2[1] - P2[0]* N2[1]/N2[0]
    x = np.linspace(0,max(data_norm[0]), 101)
    y = a*x+b
    ax.plot(x,y, label="Cancellation frequency %.2f" % z)
    print ("Equation of the line: y = %f x + %f" % (N2[1]/N2[0], P2[1] - P2[0]* N2[1]/N2[0]))

x = data_norm[0]
y = data_norm[1]
z = data_norm[2]
ax.scatter(x,y,z/float(max(z)) * 50, label='Data, size proportional to cancellations')
plt.title('Level curves of the dimensionality reduction plane')
plt.xlabel('Total delay time')
plt.ylabel('Delay frequency')
plt.ylim((0, max(data_norm[1])))
ax.legend()


# 3 dim
P,N,check = plane_plane_intersect(np.array([0., 0., 1.]), np.array([0., 0., 0.]), np.cross(eigvecs[:,maxevs[0]],eigvecs[:,maxevs[1]]), mpoint)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.set_aspect('equal')
ax.plot([mpoint[0],scalevec0[0]], [mpoint[1],scalevec0[1]],[mpoint[2],scalevec0[2]])
ax.plot([mpoint[0],scalevec1[0]], [mpoint[1],scalevec1[1]],[mpoint[2],scalevec1[2]])
ax.plot([mpoint[0],scalevec2[0]], [mpoint[1],scalevec2[1]],[mpoint[2],scalevec2[2]])
#ax.plot([P[0], P[0] + 1000*N[0] ], [P[1], P[1] + 1000*N[1] ], [P[2], P[2] + 1000*N[2] ])
x,y,z = data_norm
ax.scatter(x, y, z, alpha=0.65, c="k", s=2, label="test")
ax.axis('equal')
ax.legend()

#print ("Equation of the line: y = %f x + %f" % (N[1]/N[0], P[1] - P[0]* N[1]/N[0]))







