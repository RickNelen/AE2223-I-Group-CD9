# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:45:03 2018

@author: Laurens
"""

import lib.core as core
import numpy as np


def getdelaylist(atalevel, typ = 0, timeframe = [1988,2015], interval = 36):

    k = core.unpickle("./Data.txt")
    if typ:
        k = core.getbyType(k, typ)
        
    k = core.sortata(k, atalevel)
    
    delaylist = []
    i = 0
    h = []
    t = []
    final = []
    
    for l in np.arange(timeframe[0]*12, timeframe[1]*12+12,interval):   #overall loop for years. Till put this to 27, since we only have 2016 data until feb or so
        aa = core.datetosec(int(np.floor(l/12)),int(l%12)+1,1)
        ab = core.datetosec(int(np.floor((l+interval-1)/12)),int((l+interval-1)%12)+1,31)

        #---------------------------------------------------------------------
        for j in range(1,len(k)):                       #loop for filtering per year 
            if aa <= k[j][2] < ab:
                t.append(k[j])
        c=t[0][3]                                       #need to account for the first line
        #----------------------------------------------------------------------
        for i in range(1,len(t)):
        
            if t[i][5] == t[i-1][5]:                    #as long as the ata number is the same as the one befor
                c += t[i][3]                            #adding delaytime
                h.append(t[i][3])                       #statistical stuff
            if t[i][5] != t[i-1][5]:                    #if a new atanumber is reached
                j = []                                  #need list to create matrix
                j.append(t[i-1][5])
                j.append(c)
                delaylist.append(j)                     #add [ata,delay]
                c = t[i][3]                             #reset delay to zero for next ata
                h = []  
        #--------------------------------------------------------------------------
        delaylist = sorted(delaylist,key=lambda x: x[1] ,reverse=True)
        delaylist = delaylist[:10]
        final.append(delaylist)
        t = []
        delaylist = []
        
        
    return final, interval

    
final, interval = getdelaylist(2)

        
        
    
#FINDING HOW MANY UNIQUE ATA NUMBERS IN FINAL PER TOP 10
# =============================================================================
uniqueata = []
for y in range (len(final)):
    for l in range (10):
        uniqueata.append(final[y][l][0])
uniqueata = set(uniqueata)
uniqueata = list(uniqueata)
print 'amount of unique ATA-numbers:', len(uniqueata)
# =============================================================================




# export as csv
import csv
#import numpy as np

newl = []
intl = []
for w in range(len(final)):
    for k in range(10):
        intl.append(final[w][k][0])
        intl.append(k+1)
        intl.append(w*3+1988)
        newl.append(intl)
        intl = []
        
with open("DelayTop10_tableaulist.csv", 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for row in newl:
        wr.writerow(row)

#
#with open("DelayTop10.csv", 'wb') as myfile:
#    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#    actualmatrix = []
#    for line in final:
#        actualline= []
#        for item in line:
#            actualline.append( item[0])
#        actualmatrix.append(actualline)
#    actualmatrix = np.matrix(actualmatrix)
#    actualmatrix = actualmatrix.T # taking transpose so that the every year is a new column instead of a new row
#    for line in actualmatrix:
#        exportline = []
#        for item in line.T:
#            exportline.append(int(item))
#        wr.writerow(exportline)
#
#
#finalnp = np.array(final)
#
#ranking = []
#for ata in uniqueata:
#    ataline = []
#    ataline.append(ata)
#    for year in range(28):
#        if ata in finalnp[year,:,0]:
#            ataline.append(np.where(finalnp[year,:,0] == ata)[0][0] + 1)
#        else:
#            ataline.append(11)
#    ranking.append(ataline)
#
#ranking = np.matrix(ranking).T
#
#with open("DelayTop10Ranks.csv", 'wb') as myfile:
#    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#    for line in ranking:
#        exportline = []
#        for item in line.T:
#            exportline.append(int(item))
#        wr.writerow(exportline)
#    

#Ouput [year[ata,delaytime]]