#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:29:09 2018

@author: Misa
"""

import lib.core as core
import lib.numericals as numericals
import pickle
import time



with open("./Data.txt", "rb") as fp:   # Unpickling
   b = pickle.load(fp)
   
   
t = time.time()
# generate histograms   
histos = core.hiscalc(b,[30,31,32,34,35,36],[1,1,1,1,1,1],[[1980,2020],[1980,2020],[1980,2020],[1980,2020],[1980,2020],[1980,2020]],600)
#histos = core.hiscalc(b,[23],[2],[[1980,2020]],300)

# fit weibulls through each of them 
print numericals.fitweibull(histos)
# do stuff
elapsed = time.time() - t