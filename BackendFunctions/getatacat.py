# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\tblaha\.spyder2\.temp.py
"""

# This is legacy, not needed in any subsequent program

from numpy import floor

def getATAcat (ata, level):
    # Return the 6 digit ata category number to the specified level. Following digits will be 0
    # example --> getATAcat(651201, 3) returns 651200, getATAcat(651201, 1) returns 651000

    # I/O:
    # inputs:
    #   ata     (numpy array, length n): contains the ata numbers to be categorized
    #   level   (integer)              : ATA level,  0 for only two digit chapter, add 1 for every following digit desired

    # outputs:
    #   the category as a numpy array of length n
            
    return floor(ata*10**(-float(level))