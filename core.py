#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:05:44 2018

@author: Misa
"""

def getbyATA (data, ata):
    
    # inputs:
    #   data (list of lists or mixed type. last six fields in each sublists must be int):
    #           list containing all data lines as one sublist per data line
    #   ata  (int): ata number to be filtered. Can be 1-6 digit, but only 2,3,4 and 6 make sense, given the ATA100 definition
    
    # output:
    #   filtered: list of all sublists in the data list that comply with the ATA number specified
    
    filtered = []
    for line in data:
        i = 0
        while i < len(str(ata)):
            if int(line[-6+i]) != int(str(ata)[i]): 
                break  
            i += 1
            if i == len(str(ata)):
                filtered.append(line)
                
    return filtered

def unpickle(data):
    
    import pickle

    with open(data, "rb") as fp:   # Unpickling list all types
        Rawdata = pickle.load(fp)
        
    return Rawdata


x = unpickle("./Data.txt")