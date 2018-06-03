
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:15:10 2018

@author: Till
"""

import lib.core as core
import csv
import os


# generate lots of csv
k = core.unpickle("./Data.txt")

for top in [3,5,10]:
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
                    
                    a = core.getbyType(k, actype)
                    a = core.sortata(a, atalevel)
                    final, datelist = core.getfreqlist([beginyear,2015], interval, a, 1) # looking for delay frequency
                    
                    for w in range(len(final)):
                        for l in range(10):
                            #print w, k
                            intl.append(final[w][l][0])
                            intl.append(l+1)
                            intl.append(datelist[w])
                            newl.append(intl)
                            intl = []
                            
                    filename = "FreqTop%d_ata%d_ac%d_%d-2015_interv%d" % (top, atalevel, actype, beginyear, interval)
                    with open(os.path.join('Top10csv', filename+'.csv'), 'wb') as myfile:
                        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                        wr.writerow(['ATA', 'Rank', 'Date'])
                        for row in newl:
                            wr.writerow(row)
                    
                    timelabels = []
                    if interval == 3:
                        cycle = ['Q1', 'Q2', 'Q3', 'Q4']
                    if interval == 6:
                        cycle = ['H1', 'H2']
                    if interval == 12 or interval == 36:
                        cycle = ['']
                    
                    yearfac = interval/12.
                    
                    timelabels = []
                    for b in range(len(newl)):
                        timelabels.append(str(beginyear + int(b*yearfac)/len(cycle)) + " " + str(cycle[b%(len(cycle))]))
                    
                    core.makebumpplot(filename+'.csv', filename+'.eps', filename, timelabels, top)
                

#def frequency(k):
#    
#    freqlist = []                                       #frequency per time frame
#    t = []                                              #temporary list for storage
#    i=0
#    j=0
#    l=0
#    final = []                                          #
#    
#    s=1
#    #s = input("""which column needs to be sorted?"
#    #              1 = Frequency delays
#    #              2 = Frequency cancellations 
#    #              3 = Ratio cancellations over frequency""")
#    
#    numyear = 27
#    while l <= numyear:                                      #overall loop for years
#        aa = core.datetosec((1988+l),1,1)
#        ab = core.datetosec((1989+l),1,1)
#        #---------------------------------------------------------------------
#        for j in range(1,len(k)):                       #loop for filtering per year 
#            if aa <= k[j][2] < ab:
#                t.append(k[j])
#        cancel = t[1][4]                                #need to account for the first line
#        #c=1                                             #need to account for the first line
#        #----------------------------------------------------------------------
#        for i in range(1,len(t)):                       #loop for the details
#            if t[i][5] == t[i-1][5]:
#                c += 1                                  #frequency increase of 1
#                cancel += t[i][4]                       #number of cancellations
#            if t[i][5] != t[i-1][5]:
#                j = []
#                ratio = round((float(cancel)/c)*100 ,2) #rounding the number (number,digits)
#                j.append(t[i-1][5])                     #making the matrix
#                j.append(c)
#                j.append(cancel)
#                j.append(ratio)
#                freqlist.append(j)
#                c = 1                                   #need to account for the first new
#                cancel = t[i][4]  
#        #--------------------------------------------------------------------------
#        freqlist = sorted(freqlist,key=lambda x: x[s] ,reverse=True)
#        freqlist = freqlist[:10]
#        final.append(freqlist)                          #need to accoutn for the first new
#        l += 1
#        t = []
#        freqlist = []
#    return final



#FINDING HOW MANY UNIQUE ATA NUMBERS IN FINAL PER TOP 10
#uniqueata = []
#for y in range (len(final)):
#    for l in range (10):
#        uniqueata.append(final[y][l][0])
#uniqueata = set(uniqueata)
#uniqueata = list(uniqueata)
#print 'amount of unique ATA-numbers:', len(uniqueata)

#
## export as csv
#import csv
#
#with open("FreqTop10.csv", 'wb') as myfile:
#    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#    wr.writerow(final)

