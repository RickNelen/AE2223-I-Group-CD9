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
import datetime
import time
import copy

actype = 1
atalevel = 2
interval = 36

with open("./Data.txt", "rb") as fp:   # Unpickling list all types
   b = pickle.load(fp)

a = copy.deepcopy(b)
a = core.getbyType(a, actype)
a = core.sortata(a, atalevel)

# importing the final top 10 lists
# from DelayTop10 import getdelaylist
# arguments are the atalevel, year range and interval in months. More are possible, check the function
final_delay, datelist = core.getdelaylist(timeframe = [1988,2015], interval = 28*12, k = a) # 28*12 are the months included on the total year range


delaycutoff = 15 # min aatime to actually consider something a delay
#binsize = 5 # unused at the moment, was used for debugging

#actype = 1 # all this was used for debugging
#atalevel = 3 # 2 means chapter. higher number means more detailed ata level
#atatest = 52
#timeframe = [2011,2012]
#c = core.getbyType(b,actype) # filter by type
#c = core.getbyDate(c, timeframe)
#c = core.getbyCancelled(c, 0)


### Section on fitting stuff to the delay time distributions
j = 0
for yeardata in final_delay:
    atas = []
    for item in yeardata:
        atas.append(item[0])
    
    if len(final_delay) == 1: # if only one entry in the delay ranking, we assume the entire time range was used.
        ll = int(time.mktime(datetime.datetime.strptime('01/01/1988', "%d/%m/%Y").timetuple()))  # converted to unixtime
        ul = int(time.mktime(datetime.datetime.strptime('31/12/2015', "%d/%m/%Y").timetuple()))  # converted to unixtime
        interv = 28*12
    else:
        # lower limit of time interval for which variance needs to be computed. This is stored in here by the getdelaylist function.
        # See DelayTop10.py for details
        ll = int(time.mktime(datetime.datetime.strptime(datelist[j], "%d/%m/%Y").timetuple()))  # converted to unixtime
        # reverse engineer interval from first two entries
        interv = int(time.mktime(datetime.datetime.strptime(datelist[1], "%d/%m/%Y").timetuple())) - int(time.mktime(datetime.datetime.strptime(datelist[0], "%d/%m/%Y").timetuple()))
        ul = ll + interv
        
    c = core.getbyTimestamp(b,[ll, ul])
    
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
        hist = [delays, np.histogram(delays, range=[delaycutoff,delays.max()], bins='fd', density=True)]
    
        if ata == 32:# and j == 20:
            print "test"
            (fitbeta, mean, var, cov, chisqarr, parr) = numericals.fitweibull(hist, 1, "Ata %d -- " % ata + datetime.datetime.fromtimestamp(ll).strftime('%Y-%m') + " to " + datetime.datetime.fromtimestamp(ul).strftime('%Y-%m') + " -- Interval %d Months" % interv) # also plot it, that's what the 1 is for
        else:
            (fitbeta, mean, var, cov, chisqarr, parr) = numericals.fitweibull(hist, 0)
        
        
        final_delay[j][k].append(fitbeta[0]) # don't remember why they are 1 component lists in this case... the [0] makes it a little neater
        final_delay[j][k].append(mean[0])
        final_delay[j][k].append(var[0])
        final_delay[j][k].append(cov[0])
        final_delay[j][k].append(chisqarr[0])
        final_delay[j][k].append(parr[0])
        
        k += 1
        
    j += 1
    
# outputting to csv for representations

import csv

intl = []
newl = []
w = 0
for yeardata in final_delay:
    for k in range(10):
        #print w, k
        intl.append(yeardata[k][0])   # ata
        intl.append(k+1) # rank
        intl.append(yeardata[k][1])    # tot delay
        intl.append(datelist[w]) # date
        intl.append(yeardata[k][6][0])   # weibk
        intl.append(yeardata[k][6][1])   # weibLamb
        intl.append(yeardata[k][7])   # DelMean
        intl.append(np.sqrt(yeardata[k][8]))   # DelStdDev
        intl.append(yeardata[k][9])   # Parameter covariance matrix off-diagonal
        intl.append(yeardata[k][10])   # Chisq value
        intl.append(yeardata[k][11])   # p value
        
        newl.append(intl)
        intl = []
    w = w+1
        
with open("DelayVariancesTotalTop10.csv", 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(['ATA', 'Rank', 'TotDelay', 'Date', 'Weibk', 'WeibLamb', 'DelMean', 'DelStdDev', 'rho_xy', 'chisq', 'p'])
    for row in newl:
        wr.writerow(row)








