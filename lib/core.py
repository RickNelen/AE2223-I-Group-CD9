#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:05:44 2018

@author: Misa
"""
#Author: Till
def getbyATA (data, ata):
    
    # gets all lines in a data list fitting the ata number specified.
    # I/Os

    # inputs:
    #   data (list of lists or mixed type. last six fields in each sublists must be int):
    #           list containing all data lines as one sublist per data line
    #   ata  (int): ata number to be filtered. Can be 1-6 digit, but only 2,3,4 and 6 make sense, given the ATA100 definition
    
    # output:
    #   filtered: list of all sublists in the data list that comply with the ATA number specified
    
    # prepare input ata by padding it with zeros if necessary
    
    ata = str(ata)
    #if len(ata)%2: # pad wth leading zero if uneven
    #    ata = '0'+ata
        
    filtered = [] # initiate returned list
    
    for line in data:
        i = 0
        while i < len(ata):
            if int(line[-6+i]) != int(ata[i]): 
                break  # this breaks out of the while on the first digit mismatch between candidate and ATA number
            i += 1
            if i == len(ata): # i.e. if all digits match
                filtered.append(line)
                
    return filtered
    
#Author: Till   
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
    
#Author: Till 
def getbySerial (data, serial):
    # gets all lines in a data list that are concerning one specific aircraft type
    # I/Os

    # inputs:
    #   data (list of lists or mixed type. last six fields in each sublists must be int):
    #           list containing all data lines as one sublist per data line
    #   serial  (list or int): aircraft serial numbers to be filtered. 
    
    # output:
    #   filtered: list of all sublists in the data list that concerning the specified serial number
    
    filtered = []
    
    if not isinstance(serial, list):
        serial = [serial]
    
    for line in data:
        for numb in serial:
            if int(line[0]) == numb:
                filtered.append(line)
            
    return filtered
    
#Author: Till 
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
            
    for line in data:
        if int(line[3]) > limits[0] and int(line[3]) < limits[1]:
            filtered.append(line)
            
    return filtered

#Author: Till 
def getbyTimestamp (data, limits):
    # inputs:
    #   data (list of lists or mixed type. last six fields in each sublists must be int):
    #           list containing all data lines as one sublist per data line
    #   limits  (list of two int): lower and upper limits for the timestamp region to be filtered
    
    # output:
    #   filtered: list of all sublists in the data list that are contained in the delay interval
    
    filtered  = []
            
    for line in data:
        if int(line[2]) > limits[0] and int(line[2]) < limits[1]:
            filtered.append(line)
            
    return filtered

#Author: Till 
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
            
    for line in data:
        if int(line[4]) == cancelled:
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


#Author: Till
def hiscalc(data):
    # not using this anymore... histogram generation is now done on-site in the Variance.py

    import numpy as np
 
    histos = []
    
    for i in range(len(data)):
        
        array = np.matrix(data[i])
        
        print(np.matrix(data[i]))
        
        histos.append([array, np.matrix(np.histogram(array, bins='fd', range=(1,array.max()), density=True)) ])
        
    return histos
    


#Author: Misha
def hisplot(histos): # only the histos argument is actually used for computations, the rest is only for printing that info
                         # histos is the output of the hiscalc function
                         # ATA is the ATA number to be used in list form [1,2,3]
                         # Type is the type to be used in list form [1,2,3]
                         # Time is a list within a list [[1990,1995],[2010,2015]]

    
    import matplotlib.pyplot as plt
    
    plt.close(1)
    
    """ obsolete now, the other stuff secretly also works for just one data set
    if len(histos) == 1:
        le = len(histos[1])
        mean = sum(array)/le
        median = array[int(le/2)]
        string =  str(str(xx[0])+"-"+str(yy[0])+", "+str(tt[0])+" A: "+str(mean)+" M: "+str(median))
        plt.hist(array, bins=x,range=(1,max))
        plt.title(string)
        plt.show()
    
    else:
        """
    fig = plt.figure(num=1, figsize=(18, 12), dpi=80)
    ar = [[1,2],[2,2],[2,3],[3,3],[3,4]]
    ara = [2,4,6,9,12]
    e = 0
    nu = len(histos)
    while nu > ara[e]:
            e +=1
    
    for i in range(nu):
        """
        k[i].sort()
        if le <= max:
            True
        else:
            t = 0
            while k[i][t] <= max:
                t += 1
        """
        rawdelay = histos[i][0]
        le = len(rawdelay)
        mean = sum(rawdelay)/le
        median = rawdelay[int(le/2)]
        ax = fig.add_subplot(ar[e][0],ar[e][1],i+1)
        ax.bar(histos[i][1][1][:-1],histos[i][1][0],width=histos[i][1][1][1]-histos[i][1][1][0])
        string = str(" A: "+str(mean)+" M: "+str(median))
        ax.set_title(string)
            
        plt.tight_layout()
        plt.show()
  
#Author: Misha      
def getbyDate(data,yearrange):  #data is the usual data set
                                #Yearrange is give as a lsit with 2 entries [2000,2010]
    
    import calendar

    x = yearrange
    y = []
    filtered = []
    
    for i in range(2):
        utc = (x[i], 1, 1, 0,0,0)
        ts = calendar.timegm(utc)
        y.append(ts)
    
    for line in data:
        if line[2] >= y[0] and line[2] <= y[1]:
            filtered.append(line)
        
    return filtered
        
#Author: Misha 
def findunique(data,serial_ata,digits):    #Data is in the usual format
                                    #Serial_ata is 1 or 0, 0 for serial num and 1 for ata
                                    #Returns a list of all unique values
    
    flat = []
    j = 5+digits 

    if serial_ata == 0:
        for i in range(len(data)):
            flat.append(data[i][0])
            
    if serial_ata == 1:
        for i in range(len(data)):
            data[i][5:11] = [reduce(lambda x, y: str(x) + str(y), data[i][5:j])]
            data[i][5] = int(data[i][5])
        for i in range(len(data)):
            flat.append(data[i][5])
        
    ls = set(flat)
    ul = (list(ls))
    
    ul.sort()
    
    return ul
   
#Author: Misha 
def sortata(data,digits): 
 
    j = 5+digits 
     
    for i in range(len(data)): 
        data[i][5:11] = [reduce(lambda x, y: str(x) + str(y), data[i][5:j])] 
        data[i][5] = int(data[i][5]) 
        
    data.sort(key=lambda x: x[5]) 
     
    return data
    
    

