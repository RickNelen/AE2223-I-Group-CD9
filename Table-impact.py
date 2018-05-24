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
k = core.sortata(k, 4)
delay, date = core.getdelaylist([1988,2015],36,k)                               #getting the data ready till here

for i in range(len(delay)):                                                  #removing all the 0 delays.
    delay[i] = [x for x in delay[i] if x[-1] != 0]

impact = []
temp = []
temp2 = []
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
        temp.append(delay[i][j][0])                                             #ATA
        temp.append(delay[i][j][1])                                             #total delay
        temp.append(int(a))                                                     #freq
        temp.append(b)                                                          #arithmetric mean delay
        temp.append(int(round(stand_dev,0)))                                    #standard deviation
        temp.append(delay[i][j][4])                                             #cancellation ratio
        #temp.append(round(variance,0))
        #temp.append(combined[i][j][0])
        #temp.append(int(round(c,0)))
        
        temp2.append(temp)
        temp = []
    impact.append(temp2)
    temp2 = []
#-------------------------------------------------------------------------------finding the maximum of every loop
maximumlst = []
maximum = []
for i in range(len(impact)):
    maxtot = impact[i][0][1]
    maxfre = impact[i][0][2]
    maxgeo = impact[i][0][3]
    maxdev = impact[i][0][4]
    maxcancelrat = impact[i][0][5]
    for j in range(len(impact[i])):
        if impact[i][j][1] > maxtot:
            maxtot = impact[i][j][1]
        if impact[i][j][2] > maxfre:
            maxfre = impact[i][j][2]
        if impact[i][j][3] > maxgeo:
            maxgeo = impact[i][j][3]
        if impact[i][j][4] > maxdev:
            maxdev = impact[i][j][4]
        if impact[i][j][5] > maxcancelrat:
            maxcancelrat = impact[i][j][5]
    maximumlst.append(maxtot)
    maximumlst.append(maxfre)
    maximumlst.append(maxgeo)
    maximumlst.append(maxdev)
    maximumlst.append(maxcancelrat)
    maximum.append(maximumlst)
    maximumlst = []
#-------------------------------------------------------------------------------normalizing the table
impactgraded = []
temp2grad = []
tempgrad = []
for i in range(len(impact)):
    for j in range(len(impact[i])):
        ATA = impact[i][j][0]
        DEL = round((impact[i][j][1]/float(maximum[i][0]))*10,2)
        FRE = round((impact[i][j][2]/float(maximum[i][1]))*10,2)
        AVG = round((impact[i][j][3]/float(maximum[i][2]))*10,2)
        DEV = round((impact[i][j][4]/float(maximum[i][3]))*10,2)
        CRAT = round((impact[i][j][5]/float(maximum[i][4]))*10,2)
        MEAN = round((DEL + FRE + AVG + DEV + CRAT)/5 ,2)
        tempgrad.append(ATA)
        tempgrad.append(DEL)
        tempgrad.append(FRE)
        tempgrad.append(AVG)
        tempgrad.append(DEV)
        tempgrad.append(CRAT)
        tempgrad.append(MEAN)
        temp2grad.append(tempgrad)
        tempgrad = []
    temp2grad.sort(key= lambda x:x[6], reverse = True)
    impactgraded.append(temp2grad)
    temp2grad = []
#OUTPUT =
#period [ATA, total delay, delayfreq, cancelfreq, cancelratio, [all delays seperate]]