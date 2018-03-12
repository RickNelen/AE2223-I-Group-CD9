#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:16:20 2018

@author: Misa
"""

import pickle

with open("./Data.txt", "rb") as fp:   # Unpickling list all types
   b = pickle.load(fp)

with open("./DataType1.txt", "rb") as fp1:  # Unpickling list type 1
    b1 = pickle.load(fp1)
    
with open("./DataType2.txt", "rb") as fp2:  # Unpickling list type 2
    b2 = pickle.load(fp2)
    
with open("./DataType3.txt", "rb") as fp3:  # Unpickling list type 3
    b3 = pickle.load(fp3)
    
    
################### DATA TESTS##################################
print "First, second and last entry type 1 list"
print b1[0]
print b1[1]
print b1[-1]
print
print "First, second and last entry type 2 list"
print b2[0]
print b2[1]
print b2[-1]
print
print "First, second and last entry type 3 list"
print b3[0]
print b3[1]
print b3[-1]
################################################################
   
   
   
   
# We are going to split into 4 year increments

