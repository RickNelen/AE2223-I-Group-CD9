# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:59:21 2018

@author: Till
"""

import numpy as np
import lib.core as core
import lib.numericals as numericals
import pickle
import matplotlib.pyplot as plt

# importing the final top 10 lists
from DelayTop10 import final
final_delay = final

#
#
with open("./Data.txt", "rb") as fp:   # Unpickling list all types
   b = pickle.load(fp)


delaycutoff = 1 # min time to actually consider something a delay
#binsize = 5 # unused at the moment, was used for debugging

#actype = 1 # all this was used for debugging
#atalevel = 3 # 2 means chapter. higher number means more detailed ata level
#atatest = 52
#timeframe = [2011,2012]
#c = core.getbyType(b,actype) # filter by type
#c = core.getbyDate(c, timeframe)
#c = core.getbyCancelled(c, 0)




### Section on delay time
j = 0
for yeardata in final_delay:
    atas = []
    for item in yeardata:
        atas.append(item[0])
    
    c = core.getbyDate(b,[1988 + j, 1989 + j])
    
    i = 0
    k = 0
    for ata in atas:
        dataset = core.getbyATA(c, ata)
        
        if len(dataset) < 2: # check if emtpy, shouldnt happen for the top10 stuff
            atas.remove(ata)
            print ("had to remove an ata, cause it was (too) empty:")
            print ata
            continue # you can't fit a 2-param weibull if you only have 1 or less data points
    
        delays = []
        for i in range(len(dataset)):
            if int(dataset[i][3]) >= delaycutoff:
                delays.append(dataset[i][3])
            
        delays = np.matrix(delays)
        
        #bins = range(delays.min(), delays.max(), binsize) # used for debugging
        hist = [delays, np.histogram(delays, range=[1,delays.max()], bins='fd', density=True)]
    
        if ata == 324 and j == 20:
            (fitbeta, mean, var) = numericals.fitweibull(hist, 1)
        else:
            (fitbeta, mean, var) = numericals.fitweibull(hist, 0)
        
        final_delay[j][k].append(fitbeta)
        final_delay[j][k].append(mean)
        final_delay[j][k].append(var)
        
        k += 1
        
    j += 1