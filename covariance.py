# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:23:38 2018

@author: Till
"""

import numpy as np
#from ThreeDgraph import output
import random


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
eigvals, eigvecs = numpy.linalg.eig(covmat)

mpoint = np.mean(data, axis=1)

plot