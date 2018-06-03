# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:49:46 2018

@author: Till
"""

import numpy as np
import sklearn as sk
from sklearn.cluster import DBSCAN
#from ThreeDgraph import data
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
ax = fig.gca(projection='3d')
#ax.scatter(data[1][0], data[1][1], data[1][2])

datafordb = []
for i in range(len(data[1][0])):
    datafordb.append([data[1][0][i], data[1][1][i] , data[1][2][i] ])

datafordb = np.array(datafordb)

db = DBSCAN(eps=70, min_samples=10).fit( datafordb )
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = datafordb[class_member_mask & core_samples_mask]
    ax.scatter(xy[:, 0], xy[:, 1], xy[:, 2], 'o', c=tuple(col)#markerfacecolor=tuple(col),
             #markeredgecolor='k', markersize=14
             )

    xy = datafordb[class_member_mask & ~core_samples_mask]
    ax.scatter(xy[:, 0], xy[:, 1], xy[:, 2], 'o', c=tuple(col) #markerfacecolor=tuple(col),
             #markeredgecolor='k', markersize=6
             )

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()