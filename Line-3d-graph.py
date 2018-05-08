# -*- coding: utf-8 -*-
"""
Created on Tue May 08 16:12:29 2018

@author: Laurens
"""

import lib.core as core
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


k = core.unpickle("./Data.txt")                                                 #getting the data ready
k = core.sortata(k, 2)
delay, date = core.getdelaylist([1988,2015],36,k)                               #getting the data ready till here

for i in range(len(delay)):                                                     #removing all the 0 delays.
    delay[i] = [x for x in delay[i] if x[-1] != 0]
    
top_first_year = []
main = []
amounttopnumbers = 3
l =[[]]*amounttopnumbers


for i in range(amounttopnumbers):
    top_first_year.append(delay[0][i][0])



for i in range(len(delay)):
    for j in range(len(delay[i])):
        if delay[i][j][0] in top_first_year:
            main.append(delay[i][j])
main.sort(key= lambda x:x[0], reverse = True)

for i in range(len(top_first_year)):
    for j in range(len(main)):
        if main[j][0] == top_first_year[i]:
            l[i].append(main[j])