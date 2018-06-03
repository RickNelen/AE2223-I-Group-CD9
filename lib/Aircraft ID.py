# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:42:30 2018

@author: Laurens
"""

import pickle

Aircraft1 = []
Aircraft2 = []
Aircraft3 = []
AircraftIDdelay = []
nwlst = []
with open("./Data.txt", "rb") as fp:   # Unpickling
   b = pickle.load(fp)

b = sorted(b, key=lambda x:x[0])

c = 0
i = 0
while i < len(b):
    #dividing the list into aircrafttype
    if b[i][1] == 1:
        Aircraft1.append(b[i])
    if b[i][1] == 2:
        Aircraft2.append(b[i])
    if b[i][1] == 3:
        Aircraft3.append(b[i])
    #Computing the total delay per Aircraf ID
    if i != 0:
        if b[i][0] == b[i-1][0]:
            c += b[i][3]
        else:
            AircraftIDdelay.append(b[i][0])
            AircraftIDdelay.append(c)
            c = 0
    else:
        c += b[i][3] 
    i += 1
