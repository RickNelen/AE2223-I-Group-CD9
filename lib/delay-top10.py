# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:45:03 2018

@author: Laurens
"""

import core as core


k = core.unpickle("../Data.txt")
k = core.sortata(k,2)

delaylist = []
i=0
c=k[0][3]
h = []
for i in range(1,len(k)):
    
    if k[i][5] == k[i-1][5]:    #as long as the ata number is the same as the one befor
        c += k[i][3]            #adding delaytime
        h.append(k[i][3])       #statistical stuff
    if k[i][5] != k[i-1][5]:    #if a new atanumber is reached
        j = []                  #need list to create matrix
        j.append(k[i-1][5])
        j.append(c)
        delaylist.append(j)     #add [ata,delay]
        c = k[i][3]                   #reset delay to zero for next ata
        h = []
        
delaylist = sorted(delaylist,key=lambda x: x[1] ,reverse=True)

#Ouput [ata,delaytime]