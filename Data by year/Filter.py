#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:28:14 2018

--> filters by year by coverting the unix time to a year string ('%Y')

@author: Misa
"""

import pickle
import datetime

with open("./Data.txt", "rb") as fp:   # Unpickling
   b = pickle.load(fp)


st = []
for i in range(len(b)):
    st.append(int(datetime.datetime.fromtimestamp(b[i][2]).strftime('%Y')))
        

h = 0
for j in range(len(st)):
    if st[j] <= 1990:
        h = j
        print j
    else:
        break
        

#with open("./Data.txt", "wb+") as fp:   #Pickling
#   pickle.dump(k, fp)


