# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:15:10 2018

@author: Laurens
"""

import core as core


k = core.unpickle("../Data.txt")
k = core.sortata(k,2)

freqlist = []
i=0
c=1                                             #need to account for the first line
cancel = k[1][4]                                #need to account for the first line

for i in range(1,len(k)):
    if k[i][5] == k[i-1][5]:
        c += 1                                  #frequency
        cancel += k[i][4]                       #number of cancellations
    if k[i][5] != k[i-1][5]:
        j = []
        ratio = round((float(cancel)/c)*100 ,2) #round(number,digits)
        j.append(k[i-1][5])                     #making the matrix
        j.append(c)
        j.append(cancel)
        j.append(ratio)
        freqlist.append(j)
        c = 1                                   #need to account for the first new
        cancel = k[i][4]                        #need to accoutn for the first new

            
r = input("""which column needs to be sorted?"
              1 = Frequency delays
              2 = Frequency cancellations 
              3 = Ratio cancellations over frequency""")
if r == 1:
    freqlist = sorted(freqlist,key=lambda x: x[1] ,reverse=True)
if r == 2:
    freqlist = sorted(freqlist,key=lambda x: x[2] ,reverse=True)
if r == 3:
    freqlist = sorted(freqlist,key=lambda x: x[3] ,reverse=True)