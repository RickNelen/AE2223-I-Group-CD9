#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:05:44 2018

@author: Misa
"""


####### filtering functions ########

def getbyATA (data, ata):
    
    # gets all lines in a data list fitting the ata number specified.
    # I/Os

    # inputs:
    #   data (list of lists or mixed type. last six fields in each sublists must be int):
    #           list containing all data lines as one sublist per data line
    #   ata  (int): ata number to be filtered. Can be 1-6 digit, but only 2,3,4 and 6 make sense, given the ATA100 definition
    
    # output:
    #   filtered: list of all sublists in the data list that comply with the ATA number specified
    
    filtered = [] # initiate returned list
    
    for line in data:
        i = 0
        while i < len(str(ata)):
            if int(line[-6+i]) != int(str(ata)[i]): 
                break  # this breaks out of the while on the first digit mismatch between candidate and ATA number
            i += 1
            if i == len(str(ata)): # i.e. if all digits match
                filtered.append(line)
                
    return filtered
    
    
def getbyType (data, actype):
    # gets all lines in a data list that are concerning one specific aircraft type
    # I/Os

    # inputs:
    #   data (list of lists or mixed type. last six fields in each sublists must be int):
    #           list containing all data lines as one sublist per data line
    #   actype  (int): aircraft type id to be filtered. 1-3
    
    # output:
    #   filtered: list of all sublists in the data list that concerning the specified ac type
    
    filtered = []
    
    for line in data:
        if int(line[1]) == actype:
            filtered.append(line)
            
    return filtered
    
    
def getbySerial (data, serial):
    # gets all lines in a data list that are concerning one specific aircraft type
    # I/Os

    # inputs:
    #   data (list of lists or mixed type. last six fields in each sublists must be int):
    #           list containing all data lines as one sublist per data line
    #   serial  (int): aircraft serial number to be filtered. 
    
    # output:
    #   filtered: list of all sublists in the data list that concerning the specified serial number
    
    filtered = []
    
    for line in data:
        if int(line[0]) == serial:
            filtered.append(line)
            
    return filtered
    
    
def getbyDelay (data, limits):
    # gets all lines in a data list that are concerning one specific aircraft type
    # I/Os

    # inputs:
    #   data (list of lists or mixed type. last six fields in each sublists must be int):
    #           list containing all data lines as one sublist per data line
    #   limits  (list of two int): lower and upper limits for the delay region to be filtered
    
    # output:
    #   filtered: list of all sublists in the data list that are contained in the delay interval
    
    filtered  = []
            
    for line in data
        if int(line[3]) > limits[0] and int(line[3]) < limits[1]:
            filtered.append(line)
            
    return filtered
    
    
def getbyCancelled (data, cancelled):
    # gets all lines in a data list that are concerning one specific aircraft type
    # I/Os

    # inputs:
    #   data (list of lists or mixed type. last six fields in each sublists must be int):
    #           list containing all data lines as one sublist per data line
    #   cancelled  (int): 0 or 1, either not cancelled (0) or cancelled (1)
    
    # output:
    #   filtered: list of all sublists in the data list that comply with the cancellation
    
    filtered  = []
            
    for line in data
        if int(line[4]) == cancelled
            filtered.append(line)
            
    return filtered
    
    
####### pickling ########
    
    
def unpickle(data):
    
    import pickle

    with open(data, "rb") as fp:   # Unpickling list all types
        Rawdata = pickle.load(fp)
        
    return Rawdata


x = unpickle("./Data.txt")


    
