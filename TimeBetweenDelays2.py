# -*- coding: utf-8 -*-
"""
Created on Thu May 03 10:27:19 2018

@author: Till
"""

import numpy as np
import time
import datetime
import matplotlib.pyplot as plt
import lib.core as core
import pickle
import lib.numericals as numericals
import csv

with open("./Data.txt", "rb") as fp:   # Unpickling list all types
   b = pickle.load(fp)
   
atalst = [32, 27, 36, 21, 34, 22, 29, 24, 49, 71]

TBDF = []

i = 0
for ata in atalst:
    templst = core.getbyATA(b, ata)
    templst = core.getbyDate(templst, [2011, 2015])
    #templst = core.getbySerial(templst, 20110)
    TBDF.append([ata])
    timestamps = []
    for item in templst:
        timestamps.append(item[2])
    timestamps = np.array(timestamps)
    timestamps = np.sort(timestamps)
    #timestamps = timestamps[np.where(timestamps > 0)]
    difference = np.diff(timestamps)/(60*60*24.)
    #difference = difference[np.where(difference > 0)]
    difference = difference[np.where(difference < 365/2)]
    TBDF[i].append(difference)
    TBDF[i].append(np.histogram( difference, bins=np.linspace(0, difference.max(), 10), range=[0, difference.max()], density = True))
    (fitbeta, mean, var) = numericals.fitweibull([0, TBDF[i][2]], 0) # this [0, ...] is a quickfix, don't know exactly why
    
    TBDF[i].append(fitbeta[0]) # this [0] is a quickfix, don't know exactly why
    TBDF[i].append(mean[0])
    TBDF[i].append(var[0])
    
    i += 1
    
with open("TBDF_MeanVariance_FirstVersion.csv", 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(['ATA', 'Mean', 'Variance'])
    for row in TBDF:
        wr.writerow([row[0], row[-2], row[-1]])