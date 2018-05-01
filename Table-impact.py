# -*- coding: utf-8 -*-
"""
Created on Tue May 01 14:25:34 2018

@author: Laurens
"""

#total delay
#frequency
#mean delay
#standard deviation
#avg*total delay
import lib.core as core


#def getdelaylist(type = 0, timeframe = [1988,2015], interval = 36, k)
k = core.unpickle("./Data.txt")                                                 #getting the data ready
k = core.sortata(k, 3)
delay, date = core.getdelaylist([1988,2015],36,k)
freq = core.frequency([1988,2015],36,k)
combined = core.combining(freq, delay)                                          #getting the data ready till here

for i in range(len(combined)):                                                  #removing all the 0 delays.
    combined[i] = [x for x in combined[i] if x[-1] != 0]

impact = []
temp = []
temp2 = []
for i in range(len(combined)):
    for j in range(len(combined[i])):                                           #Needs to be switched to geometric mean
        a = len(combined[i][j][5])                                              #freq - cancellationfreq
        if combined[i][j][5][0] != 0:
            b = combined[i][j][5][0]**(1/float(a))
        if combined[i][j][5][0] == 0:
            b = 1
            #a -= 1
        for l in range(1,a):
            if combined[i][j][5][l] != 0:
                b = b*combined[i][j][5][l]**(1/float(a))                              #geo-mean
        b = int(round(b,0))
        c = combined[i][j][4] / float(a)                                        #ari mean
        d = 0
        for l in range(len(combined[i][j][5])):                                 #variance calculation
            d += (combined[i][j][5][l] - b)**2
        variance = d / float(a)
        stand_dev = variance ** (0.5)
        avg_total = (combined[i][j][4]/float(a))*combined[i][j][4]
        #------------------------------------------------------------------------normalizing
        
        #------------------------------------------------------------------------creating the table
        temp.append(combined[i][j][0])
        temp.append(combined[i][j][4])
        temp.append(a)
        temp.append(b)
        temp.append(round(stand_dev,0))
        temp.append(round(avg_total,0))
        #temp.append(round(variance,0))
        #temp.append(combined[i][j][0])
        #temp.append(int(round(c,0)))
        
        temp2.append(temp)
        temp = []
    impact.append(temp2)
    temp2 = []