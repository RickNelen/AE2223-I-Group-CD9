# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:23:38 2018

@author: Till
"""

import numpy as np
import lib.core as core
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

k = core.unpickle("./Data.txt")                                                 #getting the data ready
k = core.sortata(k, 4)
delay, date = core.getdelaylist([1988,2015],36,k)                               #getting the data ready till here
output = core.ThreeDgraph(delay, [0,1,2], 0)

columns = [[], [], []]
for line in output:
    if line[1] > 0: # can be used for filtering
        columns[0].append(line[0])
        columns[1].append(line[1])
        columns[2].append(line[2])
    
data = np.array(columns)
data = data.astype(float)
data[0] = data[0] / float(max(data[0]))
data[1] = data[1] / float(max(data[1]))
data[2] = data[2] / float(max(data[2]))

covmat = np.cov(data)   # get covariance matrix
eigvals, eigvecs = np.linalg.eig(covmat) # get eigenstuff
scaling = np.sqrt(eigvals) # get scaling factors

mpoint = np.mean(data, axis=1) # get centre point
uniformscale = 5 # just some userdefined scaling factor
scalevec0 = mpoint + scaling[0]*eigvecs[:,0]*uniformscale
scalevec1 = mpoint + scaling[1]*eigvecs[:,1]*uniformscale
scalevec2 = mpoint + scaling[2]*eigvecs[:,2]*uniformscale




b = np.array([0,1,2])
maxevs=b[np.invert(abs(eigvals)==min(abs(eigvals)))]





def plane_plane_intersect(N1,A1,N2,A2):
#    %plane_intersect computes the intersection of two planes(if any)
#    % Inputs: 
#    %       N1: normal vector to Plane 1
#    %       A1: any point that belongs to Plane 1
#    %       N2: normal vector to Plane 2
#    %       A2: any point that belongs to Plane 2
#    %
#    %Outputs:
#    %   P    is a point that lies on the interection straight line.
#    %   N    is the direction vector of the straight line
#    % check is an integer (0:Plane 1 and Plane 2 are parallel' 
#    %                              1:Plane 1 and Plane 2 coincide
#    %                              2:Plane 1 and Plane 2 intersect)
#    %
#    % Example:
#    % Determine the intersection of these two planes:
#    % 2x - 5y + 3z = 12 and 3x + 4y - 3z = 6
#    % The first plane is represented by the normal vector N1=[2 -5 3]
#    % and any arbitrary point that lies on the plane, ex: A1=[0 0 4]
#    % The second plane is represented by the normal vector N2=[3 4 -3]
#    % and any arbitrary point that lies on the plane, ex: A2=[0 0 -2]
#    %[P,N,check]=plane_intersect([2 -5 3],[0 0 4],[3 4 -3],[0 0 -2]);
#
#    %This function is written by :
#    %                             Nassim Khaled
#    %                             Wayne State University
#    %                             Research Assistant and Phd candidate
#    %If you have any comments or face any problems, please feel free to leave
#    %your comments and i will try to reply to you as fast as possible.

    #import numpy as np
    
    P=np.array([0., 0., 0.])
    N=np.cross(N1, N2);

    #%  test if the two planes are parallel
    if np.linalg.norm(N) < 10e-7:                #% Plane 1 and Plane 2 are near parallel
        V=A1-A2;
        if (np.dot(N1,V) == 0):
            check=1;                    #% Plane 1 and Plane 2 coincide
            return P,N,check
        else:
            check=0;                   #%Plane 1 and Plane 2 are disjoint
            return P,N,check


    check=2;

    #% Plane 1 and Plane 2 intersect in a line
    #%first determine max abs coordinate of cross product
    b = np.array([0,1,2])
    maxc=b[abs(N)==max(abs(N))]


    #%next, to get a point on the intersection line and
    #%zero the max coord, and solve for the other two

    d1 = -np.dot(N1, A1)  #%the constants in the Plane 1 equations
    d2 = -np.dot(N2, A2)  #%the constants in the Plane 2 equations
#
#    print d1,d2
#    print N
#    print N1
#    print N2
    
    if maxc == 0: #% intersect with x=0
        P[0]= 0
        P[1] = (d2*N1[2] - d1*N2[2])/ N[0]
        P[2] = (d1*N2[1] - d2*N1[1])/ N[0]
    elif maxc == 1: 
        
        P[0] = (d1*N2[2] - d2*N1[2])/ N[1]
        P[1] = 0
        P[2] = (d2*N1[0] - d1*N2[0])/ N[1]
    elif maxc == 2:
        P[0] = (d2*N1[1] - d1*N2[1])/ N[2]
        P[1] = (d1*N2[0] - d2*N1[0])/ N[2]
        P[2] = 0
    
    return P,N,check


# plotting

# level lines
fig2 = plt.figure()
ax = fig2.add_subplot(111)
for z in np.linspace(0,max(data[2]),5):
    P2, N2, check2 = plane_plane_intersect(np.array([0., 0., 1.]), np.array([0., 0., float(z)]), np.cross(eigvecs[:,maxevs[0]],eigvecs[:,maxevs[1]]), mpoint)
    a = N2[1]/N2[0]
    b = P2[1] - P2[0]* N2[1]/N2[0]
    x = np.linspace(0,max(data[0]), 101)
    y = a*x+b
    ax.plot(x,y, label="Cancellation frequency %.2f" % z)
    #print ("Equation of the line: y = %f x + %f" % (N2[1]/N2[0], P2[1] - P2[0]* N2[1]/N2[0]))

x = data[0]
y = data[1]
z = data[2]
ax.scatter(x,y,z/float(max(z)) * 50, label='Data, size proportional to cancellations')
plt.title('Level curves of the dimensionality reduction plane')
plt.xlabel('Total delay time')
plt.ylabel('Delay frequency')
plt.ylim((0, max(data[1])))
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
x,y,z = data
ax.scatter(x, y, z, alpha=0.65, c="k", s=2, label="test")
ax.axis('equal')
ax.legend()

print ("Equation of the line: y = %f x + %f" % (N[1]/N[0], P[1] - P[0]* N[1]/N[0]))
