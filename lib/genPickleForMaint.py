#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:27:57 2018

Takes the raw csv data, converts it into a completely numerical format, corrects the ata numbers, and pickles it.

@author: Misa
"""

import pickle

k = []

import csv
with open("../Raw_Maintenance.csv", 'rU') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in data:
        appendable = True
        newrow = []
        
        if not row[4]: # if no ac id provided
            appendable = False
        
        if row[0] == '\xef\xbb\xbf3':
            appendable = False
        
        if not row[1] or str(row[1]).lower() == "nc":
            appendable = False
            
        if not row[3]:
            appendable = False
        
        if int(row[2]) != 1:
            appendable = False
            
        
        if appendable:
            
            newrow.append( int(row[4]) )
            newrow.append( int(row[0]) )
            newrow.append( int(row[3]) )
            newrow.append( 0 )
            newrow.append( 0 )
            
            printable = False # this was for debugging
            ata = str(row[1]) # this is not anymore -3 because of the different csv structure
            #print ata
            if len(ata)%2: # pad wth leading zero if uneven
                ata = '0'+ata
            while len(ata) != 6: # enforce a 6 digit ATA number
                ata = ata+'0'
            for l in range(6): # append the new 6 ata columns
                newrow.append(int(ata[l]))
            
            if newrow[-6:] == [0,5,0,0,0,0]:
                printable = True
            
            #if printable:
            #    print row
            
            k.append(newrow)

#pickling to file
with open("./DataMaintenance.txt", "wb+") as fp:   #Pickling
   pickle.dump(k, fp)
   