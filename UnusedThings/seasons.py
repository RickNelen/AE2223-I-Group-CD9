#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:44:06 2018

@author: Misa
"""

import lib.core as core
import calendar

data = core.unpickle("./Data.txt")
data = core.getbyATA(data,30)

y = []
asp = []
asu = []
afa = []
awi = []

for i in range(25):
    

    for l in range(1,5):
        y0 = []
        months = 3*l
        monthe = 3*(l+1)
        utc = (i+1990, months, 1, 0,0,0)
        ts = calendar.timegm(utc)
        if monthe > 12:
            i += 1
            monthe = 3
        utc1 = (i+1990, monthe, 1, 0,0,0)
        ts1 = calendar.timegm(utc1)
        y0.append(ts)
        y0.append(ts1)
        for line in data:
            if y0[0] < line[2] and y0[1] > line[2]:
                if l == 1:
                    asp.append(line)
                if l == 2:
                    asu.append(line)
                if l == 3:
                    afa.append(line)
                if l == 4:
                    awi.append(line)
        y0 = []
        
        