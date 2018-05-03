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
delay, date = core.getdelaylist([1988,2015],36,k)                               #getting the data ready till here

for i in range(len(delay)):                                                  #removing all the 0 delays.
    delay[i] = [x for x in delay[i] if x[-1] != 0]

impact = []
temp = []
temp2 = []
impact_graded = []
for i in range(len(delay)):
    for j in range(len(delay[i])):                                           #Needs to be switched to geometric mean
        a = float(delay[i][j][2])                                               #freq
        if a != 0:
            b = delay[i][j][1] / a                                              #total/freq = avg
        if a == 0:
            b = 0
        b = int(round(b,0))
        d = 0
        for l in range(len(delay[i][j][5])):                                 #variance calculation
            d += (delay[i][j][5][l] - b)**2
        if a != 0:
            variance = d / a
        if a == 0:
            variance = 0
        stand_dev = variance ** (0.5)
        avg_total = b * delay[i][j][1]
        #------------------------------------------------------------------------creating the table
        temp.append(delay[i][j][0])                                          #ATA
        temp.append(delay[i][j][1])                                          #total delay
        temp.append(a)                                                          #freq
        temp.append(b)                                                          #arithmetric mean delay
        temp.append(int(round(stand_dev,0)))                                    #standard deviation
        temp.append(int(round(avg_total,0)))                                    #avg*total delay
        #temp.append(round(variance,0))
        #temp.append(combined[i][j][0])
        #temp.append(int(round(c,0)))
        
        temp2.append(temp)
        temp = []
    impact.append(temp2)
    temp2 = []
#-------------------------------------------------------------------------------finding the maximum of every loop
#maximumlst = []
#maximum = []
#for i in range(len(impact)):
#    for j in range(len(impact[i])):
#        maxtot = impact[i][0][1]
#        maxfre = impact[i][0][2]
#        maxgeo = impact[i][0][3]
#        maxdev = impact[i][0][4]
#        maxavt = impact[i][0][5]
#        if impact[i][j][1] > maxtot:
#            maxtot = impact[i][j][1]
#        if impact[i][j][2] > maxfre:
#            maxfre = impact[i][j][2]
#        if impact[i][j][3] > maxgeo:
#            maxgeo = impact[i][j][3]
#        if impact[i][j][4] > maxdev:
#            maxdev = impact[i][j][4]
#        if impact[i][j][5] > maxavt:
#            maxavt = impact[i][j][5]
#    maximumlst.append(maxtot)
#    maximumlst.append(maxfre)
#    maximumlst.append(maxgeo)
#    maximumlst.append(maxdev)
#    maximumlst.append(maxavt)
#    maximum.append(maximumlst)
#    maximumlst = []