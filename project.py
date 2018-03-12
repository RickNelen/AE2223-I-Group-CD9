#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:27:57 2018

@author: Misa
"""

import pickle

k = []

import csv
with open("./RawV02.csv", 'rU') as csvfile:
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
            
with open("./Data.txt", "wb+") as fp:   #Pickling
   pickle.dump(k, fp)


#eddit


