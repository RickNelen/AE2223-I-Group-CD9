#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 10:09:04 2018

@author: Misa
"""

import lib.core as core


#--------------------------------
# Inputs

YR = 9          #Year range (steps)
start = 1988
end = 2015
digits = 2      #ATA digits
typ = 2         #Type
atain = [21,27,29,30,32,34,36,73]

#--------------------------------
# Filtering

b = core.unpickle("./Data.txt")
b = core.getbyType(b,typ)
b = core.getbyCancelled(b,0)
b = core.sortata(b,digits)

#--------------------------------
#Random variables

current = start
flist = []
intlist = []
inlist = []
atacount = []

#--------------------------------
#While loop loops trough year range and returns list with ATA,frequency,total delay

while current + YR <= end:
    data = core.getbyDate(b,[current,current+YR])
    current += YR
    
    f = 0
    tot = 0
    
    for i in range(len(data)-1):
        if data[i][5] == data[i+1][5]:
            f += 1
            tot += data[i][3]
        else:
            f += 1
            tot += data[i][3]
            intlist.append(data[i][5])
            intlist.append(f)
            intlist.append(tot)
            inlist.append(intlist)
            intlist = []
            f = 0
            tot = 0
            atacount.append(data[i][5])
            
            
            
    flist.append(inlist)
    inlist = []
    
#--------------------------------
# Returns the average for each types

typavg = []
typtd = []
typf,typt = 0,0

for t in range(len(flist)):
    for j in range(len(flist[t])):
        typt += flist[t][j][2]
        typf += flist[t][j][1]
    typavg.append(round((float(typt)/typf),2))
    typtd.append(typt)
    typt,typf = 0,0
 
#--------------------------------
# Finds ata numbers that occure in all years and filters out that dont occure in all

ata = []

for k in range(10**digits):
    if atacount.count(k) == len(flist):
        ata.append(k)


for u in range(len(flist)):
    flist[u] = [x for x in flist[u] if x[0] in ata]


#--------------------------------
# Preserving the total dela per ata
    
intdtot = []
dtot = []

for t in range(len(flist)):
    for j in range(len(flist[t])):
        intdtot.append(flist[t][j][2])
    dtot.append(intdtot)
    intdtot = []
    
#--------------------------------
# Converts flist frequency and total delay to average delay [ATA,avg]

alist = []
intl = []
    
for g in range(len(flist)):
    for n in range(len(flist[g])):
        intl.append(round(float(flist[g][n][2])/flist[g][n][1],1))
        flist[g][n][2] = round(float(flist[g][n][2])/flist[g][n][1],1)
    alist.append(intl)
    intl = []

#--------------------------------
# Find the diferences and delets first entry

for z in range(len(flist)-1,0,-1):
    for q in range(len(flist[2])):
        flist[z][q][1] = flist[z][q][1] - flist[z-1][q][1]
        
typavg2 = list(typavg)

for a in range(len(typavg)-1,0,-1):
    typavg[a] = round((typavg[a] - typavg[a-1]),1)

del flist[0],typavg[0]

#--------------------------------
# Calculated IB 

ib = []
intib = []
for n in range(len(flist)):
    for m in range(len(flist[n])):
        if typavg[n] == 0 or flist[n][m][1] == 0:
            intib.append(0)
        else:
            intib.append(round((typavg[n]/flist[n][m][1]),4))
    ib.append(intib)
    intib = []

#--------------------------------
# Calculating IC

ic = []
intic = []

for n in range(len(flist)):
    for m in range(len(flist[n])):
        intic.append(round((ib[n][m]*(flist[n][m][2]/typavg2[n]))*100,2))
    ic.append(intic)
    intic = []
    
#--------------------------------
# Calculating a new metric IB*(total delay from 1 ata/total delay of plane type)

icn = []
inticn = []

for n in range(len(flist)):
    for m in range(len(flist[n])):
        inticn.append(round((ib[n][m]*(float(dtot[n][m])/typtd[n])*1000),2))
    icn.append(inticn)
    inticn = []
    
#--------------------------------
# Calculating new metric of toatal delay of ata times the average

nm = []
inticn = []

for n in range(len(alist)):
    for m in range(len(alist[n])):
        inticn.append(round((dtot[n][m]*alist[n][m])/100000,2))
    nm.append(inticn)
    inticn = []

#--------------------------------
# Getting list for specific ATA numbers

atain = [x for x in atain if x in ata]

apl = []
for i in range(len(ata)):
    if ata[i] in atain:
        apl.append(i)
        
        

row = []
final = []

for i in range(len(atain)):
    row = [start,atain[i],0,0,0]
    row.append(nm[0][apl[i]])
    final.append(row)
    row= []
        

for i in range(len(ic)):
    for k in range(len(atain)):
        row.append(start+YR*(i+1))
        row.append(atain[k])
        row.append(ib[i][apl[k]])
        row.append(ic[i][apl[k]])
        row.append(icn[i][apl[k]])
        row.append(nm[i+1][apl[k]])
        final.append(row)
        row = []
        
