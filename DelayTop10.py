# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:45:03 2018

@author: Laurens
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
                    final, datelist = core.getdelaylist([beginyear,2015], interval, a)
                    
                    for w in range(len(final)):
                        for l in range(10):
                            #print w, k
                            intl.append(final[w][l][0])
                            intl.append(l+1)
                            intl.append(datelist[w])
                            newl.append(intl)
                            intl = []
                            
                    filename = "DelayTop%d_ata%d_ac%d_%d-2015_interv%d" % (top, atalevel, actype, beginyear, interval)
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
                




#generate lots of plots from these csv's



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