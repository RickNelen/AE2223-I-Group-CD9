#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:27:57 2018

Takes the raw csv data, converts it into a completely numerical format, corrects the ata numbers, and pickles it.

@author: Misa
"""

import pickle
import datetime

k = []

import csv
with open("./Raw_Delay.csv", 'rU') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in data:
        
        if row[-1] == "FALSE":
            row[-1] = 0
        else:
            row[-1] = 1
        if row[-3].lower() == "nc":
            row[-3] = 0
            
        for i in range(len(row)):
            if row[i] == "":
                row[i] = 0
                
        row = [int(c) for c in row]
        #if row [-3] != 0:
        k.append(row)

for i in range(len(k)):
    c = str(k[i][-3])
    c = list(c)
    while len(c) != 6: # enforce a 6 digit ATA number
        c.append(0)
    del k[i][-3]# get rid of the original ata number
    for l in range(len(c)): # append the new 6 ata columns
        k[i].append(int(c[l]))

#pickling to file
with open("./Data.txt", "wb+") as fp:   #Pickling
   pickle.dump(k, fp)
   