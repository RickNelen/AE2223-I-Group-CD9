# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:45:03 2018

@author: Laurens
"""

import lib.core as core


k = core.unpickle("./Data.txt")
k = core.sortata(k,4)

delaylist = []
i=0
h = []
t = []
l = 0
final = []
        
delaylist = sorted(delaylist,key=lambda x: x[1] ,reverse=True)

#Ouput [ata,delaytime]

while l <= 27:                                      #overall loop for years. Till put this to 27, since we only have 2016 data until feb or so
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
    l += 1
    t = []
    delaylist = []
    
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
