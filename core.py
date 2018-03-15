#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:05:44 2018

@author: Misa
"""
#Author: Till
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

#Author: Misha
def unpickle(file): # Enter file directory as a "string", use "./filename.txt" if it is in the same folder 
                    # Use "../filename.txt" if it is one directory above
    
    import pickle

    with open(file, "rb") as fp:
        Rawdata = pickle.load(fp)
        
    return Rawdata

#Author: Misha
def pickle(file,data):  # Enter file directory as a "string", use "./filename.txt" if it is in the same folder 
                        # Use "../filename.txt" if it is one directory above
                        # Data is the list that is to be saved
                        # This creats a new file if it does not find an existing one with the name given
    
    import pickle
    
    with open(file, "wb+") as fp:
        pickle.dump(data, fp)
        
#Author: Misha
def datetosec(year,month,day): 
    
    import calendar

    utc = (year, month, day, 0,0,0)
    timestamp = calendar.timegm(utc)
    
    return timestamp


