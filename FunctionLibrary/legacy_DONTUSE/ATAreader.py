#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:12:26 2018

Takes an existing pickle and removes the integer ATA number and adds 6 new columns for every digit

@author: Misa
"""

import pickle

with open("./Data.txt", "rb") as fp:
   b = pickle.load(fp)

for i in range(len(b)):
    c = str(b[i][-3])
    c = list(c)
    while len(c) != 6: # enforce a 6 digit ATA number
        c.append(0)
    del b[i][-3]# get rid of the original ata number
    for l in range(len(c)): # append the new 6 ata columns
        b[i].append(int(c[l]))

with open("./Data.txt", "wb+") as fp:   #Pickling
   pickle.dump(b, fp)
   
