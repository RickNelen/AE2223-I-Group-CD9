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
    #   serial  (int): aircraft serial number to be filtered. 
    
    # output:
    #   filtered: list of all sublists in the data list that concerning the specified serial number
    
    filtered = []
    
    for line in data:
        if int(line[0]) == serial:
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

#Author: Misha
def hisplot(ATA,Type,Time,max): #ATA is the ATA number to be used in list form [1,2,3]
                                #Type is the type to be used in list form [1,2,3]
                                #Time is a list within a list [[1990,1995],[2010,2015]]
                                #Make sure that all the lists given have the same length
                                #If only one graph is wanted enter that data between square brackets [number]
                                #If certain filtering is not needed then type 0 in square brackets [0] use [0,0] for time
                                #Max is the maximum value displayed on the x axis 
    
    import matplotlib.pyplot as plt
    
    b = unpickle("./Data.txt")
    
    xx = ATA
    yy = Type
    tt = Time
    
    k = []
    
    for i in range(len(xx)):
        
        x = xx[i]
        y = yy[i]
        t = tt[i]
        
        data = b
        
        if x != 0:
            data = getbyATA(data,int(x))
        if y != 0:
            data = getbyType(data,int(y))
        if t != [0,0]:
            data = getbyDate(data,t)
    
        array = []
        
        for i in range(len(data)):
            array.append(data[i][3])
        
        k.append(array)
        
    plt.close(1)
    
    if len(xx) == 1:
            array = k[0]
            array.sort()
            le = len(array)
            if le <= max:
                True
            else:
                t = 0
                while array[t] <= max:
                    t += 1
            mean = sum(array)/le
            median = array[int(le/2)]
            string =  str(str(xx[0])+"-"+str(yy[0])+", "+str(tt[0])+" A: "+str(mean)+" M: "+str(median))
            plt.hist(array, bins=x,range=(1,max))
            plt.title(string)
            plt.show()
    
    else:
        fig = plt.figure(num=1, figsize=(18, 12), dpi=80)
        nu = len(xx)
        ar = [[1,2],[2,2],[2,3],[3,3],[3,4]]
        ara = [2,4,6,9,12]
        e = 0
        while nu > ara[e]:
                e +=1
        
        for i in range(len(xx)):
            k[i].sort()
            le = len(k[i])
            if le <= max:
                True
            else:
                t = 0
                while k[i][t] <= max:
                    t += 1
            mean = sum(k[i])/le
            median = k[i][int(le/2)]
            ax = fig.add_subplot(ar[e][0],ar[e][1],i+1)
            ax.hist(k[i], bins="auto",range=(1,max))
            string = str(str(xx[i])+"-"+str(yy[i])+", "+str(tt[i])+" A: "+str(mean)+" M: "+str(median))
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
def findunigue(data,serial_ata):    #Data is in the usual format
                                    #Serial_ata is 1 or 0, o for serial num and 1 for ata
                                    #Returns a list of all unique values
    
    flat = []

    if serial_ata == 0:
        for i in range(len(data)):
            flat.append(data[i][0])
            
    if serial_ata == 1:
        for i in range(len(data)):
            data[i][5:11] = [reduce(lambda x, y: str(x) + str(y), data[i][5:11])]
            data[i][5] = int(data[i][5])
        for i in range(len(data)):
            flat.append(data[i][5])
        
    ls = set(flat)
    ul = (list(ls))
    
    ul.sort()
    
    return ul
    
    
    
    