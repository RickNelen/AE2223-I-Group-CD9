# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:45:03 2018

@author: Laurens
"""

import lib.core as core
import numpy as np
import datetime


<<<<<<< Updated upstream
def getdelaylist(atalevel, type = 0, timeframe = [1988,2015], interval = 36): # interval in months, type = 0 means all types

    k = core.unpickle("./Data.txt")
    if type:
        k = core.getbyType(k, type)
        
    k = core.sortata(k, atalevel)
    
=======
k = core.unpickle("./Data.txt")
k = core.getbyType(k,1)
k = core.sortata(k,3)

delaylist = []
i=0
t = []
final = []
typelist = []
typ = 1
numyear = 28

for l in range(numyear+1):                              #overall loop for years. Till put this to 27, since we only have 2016 data until feb or so
    aa = core.datetosec((1988+l),1,1)
    ab = core.datetosec((1989+l),1,1)
    #---------------------------------------------------------------------
    for j in range(1,len(k)):                       #loop for filtering per year 
        if aa <= k[j][2] < ab:
            t.append(k[j])
    c=t[0][3]                                       #need to account for the first line
    #----------------------------------------------------------------------
    for i in range(1,len(t)):
    
        if t[i][5] == t[i-1][5]:                    #as long as the ata number is the same as the one befor
            c += t[i][3]                            #adding delaytime
        if t[i][5] != t[i-1][5]:                    #if a new atanumber is reached
            j = []                                  #need list to create matrix
            j.append(t[i-1][5])
            j.append(c)
            delaylist.append(j)                     #add [ata,delay]
            c = t[i][3]                             #reset delay to zero for next ata
              
    #--------------------------------------------------------------------------
    delaylist = sorted(delaylist,key=lambda x: x[1] ,reverse=True)
    #delaylist = delaylist[:10]
    final.append(delaylist)                          
    t = []
>>>>>>> Stashed changes
    delaylist = []
    i = 0
    h = []
    t = []
    final = []
    datelist = []
    
    for l in np.arange(timeframe[0]*12, timeframe[1]*12+12,interval):   #overall loop for years. Till put this to 27, since we only have 2016 data until feb or so
        aa = core.datetosec(int(np.floor(l/12)),int(l%12)+1,1) # lower limit converted to unix
        ab = core.datetosec(int(np.floor((l+interval-1)/12)),int((l+interval-1)%12)+1,31) # upper limit in unix
        
        # the lower limit is appended to the array outputting the dates used!
        # This needs to be kept in mind when evaluatign and drawing conclusions!!!
        datelist.append(datetime.datetime.fromtimestamp(aa).strftime('%d/%m/%Y')) 
        
        
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
        
        
    return final, datelist

    


        
        
    
#FINDING HOW MANY UNIQUE ATA NUMBERS IN FINAL PER TOP 10
# =============================================================================
#uniqueata = []
#for y in range (len(final)):
#    for l in range (10):
#        uniqueata.append(final[y][l][0])
#uniqueata = set(uniqueata)
#uniqueata = list(uniqueata)
#print 'amount of unique ATA-numbers:', len(uniqueata)
# =============================================================================




# this uses the above function to generate a lot of csv's for top 10s in a lot of year ranges and categories.


def gencsvs(): # runs for like 10mins
# export as csv
    import csv
    
    for atalevel in range(2,5):
        for beginyear in [1988, 2011, 2014]:
            for actype in range(1,4):
                    for interval in [3,6,12,36]:
                        
                        newl = []
                        intl = []
                        if actype == 3 and beginyear < 1995:
                            beginyear = 1995
                        if (beginyear == 1988 or (actype == 3 and beginyear == 1995)) and interval <= 6:
                            continue
                        final, datelist = getdelaylist(atalevel, actype, [beginyear,2015], interval)
                        
                        for w in range(len(final)):
                            for k in range(10):
                                #print w, k
                                intl.append(final[w][k][0])
                                intl.append(k+1)
                                intl.append(datelist[w])
                                newl.append(intl)
                                intl = []
                                
                        with open("DelayTop10_ata%d_ac%d_%d-2015_interv%d.csv" % (atalevel, actype, beginyear, interval), 'wb') as myfile:
                            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                            wr.writerow(['ATA', 'Rank', 'Date'])
                            for row in newl:
                                wr.writerow(row)
                                
    return 0

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