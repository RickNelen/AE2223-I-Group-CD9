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
with open("../Raw_Delay.csv", 'rU') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in data:
        appendable = True
        
        if row[-1].lower() == "false" and (row[-2] == "" or row[-2] == 0):  # forget rows with no cancellation but also no delay time
            appendable = False
            
        if row[-3].lower() == "nc": # forget rows with no ata number
            appendable = False
        
        if row[-1].lower() == "false": # change cancellations into numerical
            row[-1] = 0
        else:
            row[-1] = 1
           
        for i in range(len(row)):
            if row[i] == "":
                row[i] = 0
                    
        if appendable:
            printable = False # this was for debugging
            ata = str(row[-3])
            if len(ata)%2: # pad wth leading zero if uneven
                ata = '0'+ata
            while len(ata) != 6: # enforce a 6 digit ATA number
                ata = ata+'0'
            del row[-3] # delete old format from data
            for l in range(6): # append the new 6 ata columns
                row.append(int(ata[l]))
        
            row = [int(c) for c in row] # converts stuff to int
            
            if row[-6:] == [0,5,0,0,0,0]:
                printable = True
            
            #if printable:
            #    print row
            
            k.append(row)

#pickling to file
with open("./Data.txt", "wb+") as fp:   #Pickling
   pickle.dump(k, fp)
   