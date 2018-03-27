# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 08:22:57 2018

@author: Till
"""
import numpy as np
import lib.core as core
import lib.numericals as numericals
import pickle


with open("./Data.txt", "rb") as fp:   # Unpickling list all types
   b = pickle.load(fp)
   


actype = 1 # define this
atalevel = 2 # 2 means chapter. higher number means more detailed ata level
timeframe = [1980,2020]

b = core.getbyType(b,actype) # filter by type



# main loop, probably takes forever
ata = []
data = []
means = []
variances = []
histos = []

for atanum in range(1,10**atalevel): # 1 to 99 in steps of 1
    atastr = str(atanum)
    while len(atastr) < atalevel:
        atastr = '0'+atastr
    filtered = core.getbyATA(b,atastr)
    if len(filtered):
        ata.append(atastr)
        data.append(filtered)

histos = core.hiscalc(b,ata,len(ata)*[actype],len(ata)*[timeframe],600)
print numericals.fitweibull(histos)





        