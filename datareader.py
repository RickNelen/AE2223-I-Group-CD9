#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:16:20 2018

@author: Misa
"""


import pickle

with open("./Data.txt", "rb") as fp:   # Unpickling
   b = pickle.load(fp)


# this is a comment
   
# We are going to split into 4 year increments