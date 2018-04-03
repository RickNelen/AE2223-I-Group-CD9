# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:15:10 2018

@author: Laurens
"""

import core as core


k = core.unpickle("../Data.txt")
k = core.sortata(k,4)


freqlist = []                                       #frequency per time frame
t = []                                              #temporary list for storage
i=0
j=0
l=0
final = []                                          #

s=1
#s = input("""which column needs to be sorted?"
#              1 = Frequency delays
#              2 = Frequency cancellations 
#              3 = Ratio cancellations over frequency""")


while l <= 28:                                      #overall loop for years
    aa = core.datetosec((1988+l),1,1)
    ab = core.datetosec((1989+l),1,1)
    #---------------------------------------------------------------------
    for j in range(1,len(k)):                       #loop for filtering per year 
        if aa <= k[j][2] < ab:
            t.append(k[j])
    cancel = t[1][4]                                #need to account for the first line
    c=1                                             #need to account for the first line
    #----------------------------------------------------------------------
    for i in range(1,len(t)):                       #loop for the details
        if t[i][5] == t[i-1][5]:
            c += 1                                  #frequency increase of 1
            cancel += t[i][4]                       #number of cancellations
        if t[i][5] != t[i-1][5]:
            j = []
            ratio = round((float(cancel)/c)*100 ,2) #rounding the number (number,digits)
            j.append(t[i-1][5])                     #making the matrix
            j.append(c)
            j.append(cancel)
            j.append(ratio)
            freqlist.append(j)
            c = 1                                   #need to account for the first new
            cancel = t[i][4]  
    #--------------------------------------------------------------------------
    freqlist = sorted(freqlist,key=lambda x: x[s] ,reverse=True)
    freqlist = freqlist[:10]
    final.append(freqlist)                          #need to accoutn for the first new
    l += 1
    t = []
    freqlist = []
    
#FINDING HOW MANY UNIQUE ATA NUMBERS IN FINAL PER TOP 10
uniqueata = []
for y in range (len(final)):
    for l in range (10):
        uniqueata.append(final[y][l][0])
uniqueata = set(uniqueata)
uniqueata = list(uniqueata)
print 'amount of unique ATA-numbers:', len(uniqueata)
