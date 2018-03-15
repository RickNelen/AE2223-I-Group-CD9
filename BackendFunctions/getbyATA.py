# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:13:01 2018

@author: tblaha
"""

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