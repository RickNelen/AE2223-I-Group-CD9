#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:29:09 2018

@author: Misa
"""

import lib.core as core
import time


core.hisplot([32,32,32,32],[1,2,3,2],[[2000,2003],[2003,2006],[2006,2009],[2009,2012]],600)

#data = core.unpickle("./Data.txt")
#
#s = time.time()
#l = core.sortata(data,4)
#e = time.time()
#print e -s
#
#
#s = time.time()
#k = core.findunigue(data, 1,4)
#e = time.time()
#print e -s

