# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:48:10 2018

@author: Laurens
"""
import lib.core as core

k = core.unpickle("./Data.txt")                                                 #getting the data ready
k = core.sortata(k, 4)
delay, date = core.getdelaylist([1988,2015],36,k)                               #getting the data ready till here
output = core.ThreeDgraph(delay, 3, 0)

