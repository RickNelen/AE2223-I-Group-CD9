#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:12:26 2018

@author: Misa
"""

import pickle

with open("./Data.txt", "rb") as fp:
   b = pickle.load(fp)
   
for i in range(len(b)):
    c = str(b[i][-3])
    c = list(c)
    while len(c) != 6:
        c.append(0)
    del b[i][-3]
    for l in range(len(c)):
        b[i].append(int(c[l]))

with open("./Data.txt", "wb+") as fp:   #Pickling
   pickle.dump(b, fp)
   
