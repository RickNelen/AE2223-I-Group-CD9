#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:29:09 2018

@author: Misa
"""

import lib.core as core
<<<<<<< Updated upstream
import time


#core.hisplot([32,32,32,32],[2,2,2,2],[[2000,2003],[2003,2006],[2006,2009],[2009,2012]],200)

data = core.unpickle("./Data.txt")

s = time.time()
l = core.sortata(data,4)
e = time.time()
print e -s


s = time.time()
k = core.findunigue(data, 1,4)
e = time.time()
print e -s
=======
import lib.numericals as numericals
import numpy as np
import pickle

with open("./Data.txt", "rb") as fp:   # Unpickling
   b = pickle.load(fp)
>>>>>>> Stashed changes

#histos = core.hiscalc(b,[32,31],[2,1],[[2000,2003],[2000,2003]],300)
histos = core.hiscalc(b,[32],[2],[[2000,2003]],300)

#core.hisplot(histos,[32],[2],[[2000,2003]])




def weibull(beta, x):
    return beta[0]/beta[1] * (x/beta[1])**(beta[0]-1) * np.exp(-1*(x/beta[1])**beta[0]) 

numericals.lstsquares(weibull, 2, np.array([1,20]), np.concatenate( ( np.array([histos[0][1][1][0:-1]]).T, np.array([histos[0][1][0]]).T) , axis=1) )