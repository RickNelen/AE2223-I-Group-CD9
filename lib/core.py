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
    beun = data
    for i in range(len(data)): 
        beun[i][5:11] = [reduce(lambda x, y: str(x) + str(y), beun[i][5:j])] 
        beun[i][5] = int(beun[i][5]) 
        
    data.sort(key=lambda x: x[5]) 
     
    return beun



def getfleetsize(timeframe , interval, k):
    import numpy as np
    import datetime
    
    fleetsize = []
    fleetsize1 = []
    datelist = []
    for l in np.arange(timeframe[0]*12, timeframe[1]*12+12,interval):   #overall loop for years. Till put this to 27, since we only have 2016 data until feb or so
        aa = datetosec(int(np.floor(l/12)),int(l%12)+1,1) # lower limit converted to unix
        ab = datetosec(int(np.floor((l+interval-1)/12)),int((l+interval-1)%12)+1,31) # upper limit in unix
        t = []
        
        datelist.append(datetime.datetime.fromtimestamp(aa).strftime('%d/%m/%Y')) 
        
        for j in range(1,len(k)):                                                   #loop for filtering per year 
            if aa <= k[j][2] < ab:
                t.append(k[j][0])
    
        t = list(set(t))
        t.sort(key= lambda x:x)
        fleetsize.append(len(t))
        fleetsize1.append(t)
        t = []
        
    return fleetsize, fleetsize1

#def getdelaylist(type = 0, timeframe = [1988,2015], interval = 36, k):
def getdelaylist(timeframe , interval, k): # interval in months, type = 0 means all types
    import numpy as np
    import datetime
    
    final = []
    datelist = []

    for l in np.arange(timeframe[0]*12, timeframe[1]*12+12,interval):   #overall loop for years. Till put this to 27, since we only have 2016 data until feb or so
        aa = datetosec(int(np.floor(l/12)),int(l%12)+1,1) # lower limit converted to unix
        ab = datetosec(int(np.floor((l+interval-1)/12)),int((l+interval-1)%12)+1,31) # upper limit in unix
        t = []
        # the lower limit is appended to the array outputting the dates used!
        # This needs to be kept in mind when evaluatign and drawing conclusions!!!
        datelist.append(datetime.datetime.fromtimestamp(aa).strftime('%d/%m/%Y')) 
        
        
        #---------------------------------------------------------------------
        for j in range(1,len(k)):                       #loop for filtering per year 
            if aa <= k[j][2] < ab:
                t.append(k[j])
    #        c=t[0][3]                                       #need to account for the first line
        #----------------------------------------------------------------------
        temp = [t[0][5], t[0][3]]
        cancel = 0
        almostfinal = []
        
        for i in range(1,len(t)):
            if t[i][5] == t[i-1][5]:
                if t[i][4] == 0:
                    temp.append(t[i][3])
                if t[i][4] == 1:
                    cancel += 1
            if t[i][5] != t[i-1][5]:
                atadel = [temp[0], sum(temp[1:len(temp)]), (len(temp)-1), cancel, round((float(cancel)/((len(temp)-1)+cancel)),2)]#pure chaos
                atadel.append(temp[1:len(temp)])
                almostfinal.append(atadel)
                if t[i][4] == 0:
                    temp = [t[i][5], t[i][3]]
                    cancel = 0
                if t[i][4] == 1:
                    temp = [t[i][5]]
                    cancel = t[i][4]
    #        if i == (len(t)-1):
                
        atadel = [temp[0], sum(temp[1:len(temp)]), (len(temp)-1), cancel, round((float(cancel)/((len(temp)-1)+cancel)),2)]#pure chaos
        atadel.append(temp[1:len(temp)])
        almostfinal.append(atadel)
        almostfinal.sort(key=lambda x: x[1], reverse=True)
        atadel = []
        final.append(almostfinal)
        
        #FINDING HOW MANY UNIQUE ATA NUMBERS IN FINAL PER TOP 10
        # =============================================================================
        #uniqueata = []
        #for y in range (len(final)):
        #    for l in range (10):
        #        uniqueata.append(final[y][l][0])
        #uniqueata = set(uniqueata)
        #uniqueata = list(uniqueata)
        #print 'amount of unique ATA-numbers:', len(uniqueata)
        # =============================================================================
        
    return final, datelist

def getfreqlist(timeframe , interval, k, s): # s is the lambda key:
                                               # 1 for freqency delays
                                               # 2 for Frequency cancellations
                                               # 3 Ratio cancellations over frequency
    ### author, Till & Laurens ###
    import numpy as np
    import datetime
    
    cancellist = []                                       #frequency per time frame
    t = []                                              #temporary list for storage
    i=0
    j=0
    l=0
    final = []         
    datelist = []                                 #
    
    for l in np.arange(timeframe[0]*12, timeframe[1]*12+12,interval):   #overall loop for years. Till put this to 27, since we only have 2016 data until feb or so
        t = []
        freqlist = []
        aa = datetosec(int(np.floor(l/12)),int(l%12)+1,1) # lower limit converted to unix
        ab = datetosec(int(np.floor((l+interval-1)/12)),int((l+interval-1)%12)+1,31) # upper limit in unix
        t = []
        # the lower limit is appended to the array outputting the dates used!
        # This needs to be kept in mind when evaluatign and drawing conclusions!!!
        datelist.append(datetime.datetime.fromtimestamp(aa).strftime('%d/%m/%Y')) 
        
        #---------------------------------------------------------------------
        for j in range(1,len(k)):                       #loop for filtering per year 
            if aa <= k[j][2] < ab:
                t.append(k[j])
    #        c=t[0][3]                                       #need to account for the first line
        #----------------------------------------------------------------------
        cancel = t[1][4]                                #need to account for the first line
        c=1                                             #need to account for the first line
        #----------------------------------------------------------------------
        for i in range(1,len(t)):                       #loop for the details
            if t[i][5] == t[i-1][5]:
                c += 1                                  #frequency increase of 1
                cancel += t[i][4]                       #number of cancellations
            if t[i][5] != t[i-1][5]:
                j = []
                ratio = round((float(cancel)/c)*100 ,2) #rounding the number (number,digits)
                j.append(t[i-1][5])                     #making the matrix
                j.append(c)
                j.append(cancel)
                j.append(ratio)
                freqlist.append(j)
                c = 1                                   #need to account for the first new
                cancel = t[i][4]
        #--------------------------------------------------------------------------
        cancellist = sorted(freqlist,key=lambda x: x[s] ,reverse=True)
        cancellist = cancellist[:10]
        final.append(cancellist)                          #need to accoutn for the first new
        l += 1
    return final, datelist

    
def makebumpplot(csvname, epsname, title, timelabels, top):  # assumed input csv path "Top10csv", assumed image output path "results/rankings"
    
    
    from matplotlib import pyplot as plt
    import os
    import csv
    import numpy as np
    
    
      
    with open(os.path.join('Top10csv', csvname), 'rb') as csvfile:
        ranking_raw = csv.reader(csvfile, delimiter=';', quotechar='|')
        ranking = []
        i = 0
        for line in ranking_raw:
            split = line[0].split(',');
            if i > 0 and int(split[1].split('"')[1]) <= top:
                items = []
                for item in split:
                    items.append(item.split('"')[1]) # because python sucks
                ranking.append(items)
            i += 1
    
    
    n = len(ranking) / top
    
    atasint = []
    for line in ranking:
        if int(line[0]) not in atasint:
            atasint.append(int(line[0]))
            
    atas = []
    for ata in atasint:
        atas.append([ata])
    
    
    k = 0
    for ata in atas:
        for i in range(n):
            temp = 0
            for j in range(top):
                idx = i * top + j
                if ata[0] == int(ranking[idx][0]):
                    temp = int(ranking[idx][1])
            if temp != 0:
                atas[k].append(temp)
            else:
                atas[k].append(float('nan'))
        k += 1
    
    atas = np.matrix(atas)
    atas = atas.T
    
    plt.close()
    plt.figure(figsize=(15./11. + 15./11.*n, 9./11 + 9./11 * top))
    plt.plot(atas[1:,:])
    
    for pythonsucks in range(len(atasint)):
        plt.scatter(np.arange(n), np.array(atas[1:,pythonsucks]), 800, marker='o', edgecolors = 'k')
        
        for x,y in zip( np.arange(n), np.array(atas[1:,pythonsucks]) ):
            plt.annotate(
                str(int(np.array(atas[0,pythonsucks]))),
                xy=(x, y[0]), xytext=(0, 0),
                textcoords='offset points', ha='center', va='center',
                size = 'x-large',
                color = 'white'
                #bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                #arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0')
                )
            
    plt.ylim(top+1,0)
    plt.ylabel('Rank')
    plt.title(title)
    plt.yticks(np.arange(top) + 1, np.arange(top) + 1 )
    plt.xticks(np.arange(n), timelabels, rotation=90)
    plt.savefig(os.path.join('Results','rankings',epsname), format='eps', dpi=1000)
    #plt.show()
    
    
    
def ThreeDgraph(delay, periodnumber, graph):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits import mplot3d
    
    for i in range(len(delay)):                                                     #removing all the 0 delays.
        delay[i] = [x for x in delay[i] if x[2] != 0]
    output = []
    
    for year in range(len(delay)):
        cmap = []
        x1 = []
        x2 = []
        x3 = []
        x4 = []
        x5 = []
        y1 = []
        y2 = []
        y3 = []
        y4 = []
        y5 = []
        z1 = []
        z2 = []
        z3 = []
        z4 = []
        z5 = []
        Aircraftgen = [0,1,2,3,4,5,6,7,8,9,10,11,12,14,18] #->blue
        airframesystem = [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50] #-> pink
        structure = [51,52,53,54,55,56,57] #-> orange
        proprotor = [60,61,62,63,64,65,66,67] #-> red
        powerplant = [70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85.91,92] #-> black
        for i in range(len(delay[year])):
            if int(str(delay[year][i]).strip('[')[:2]) in Aircraftgen:
                cmap.append('b')
                x1.append(delay[year][i][1])#/delay[year][i][2])
                y1.append(delay[year][i][2])
                z1.append(delay[year][i][3])#/float(delay[year][i][3]+delay[year][i][2]))
            if int(str(delay[year][i]).strip('[')[:2]) in airframesystem:
                cmap.append('m')
                x2.append(delay[year][i][1])#/delay[year][i][2])
                y2.append(delay[year][i][2])
                z2.append(delay[year][i][3])#/float(delay[year][i][3]+delay[year][i][2]))
            if int(str(delay[year][i]).strip('[')[:2]) in structure:
                cmap.append('g')
                x3.append(delay[year][i][1])#/delay[year][i][2])
                y3.append(delay[year][i][2])
                z3.append(delay[year][i][3])#/float(delay[year][i][3]+delay[year][i][2]))
            if int(str(delay[year][i]).strip('[')[:2]) in proprotor:
                cmap.append('r')
                x4.append(delay[year][i][1])#/delay[year][i][2])
                y4.append(delay[year][i][2])
                z4.append(delay[year][i][3])#/float(delay[year][i][3]+delay[year][i][2]))
            if int(str(delay[year][i]).strip('[')[:2]) in powerplant:
                cmap.append('k')      
                x5.append(delay[year][i][1])#/delay[year][i][2])
                y5.append(delay[year][i][2])
                z5.append(delay[year][i][3])#/float(delay[year][i][3]+delay[year][i][2]))
        
        data1 = (np.asarray(x1),np.asarray(y1),np.asarray(z1))
        data2 = (np.asarray(x2),np.asarray(y2),np.asarray(z2))
        data3 = (np.asarray(x3),np.asarray(y3),np.asarray(z3))
        data4 = (np.asarray(x4),np.asarray(y4),np.asarray(z4))
        data5 = (np.asarray(x5),np.asarray(y5),np.asarray(z5))
        data = (data1,data2,data3,data4,data5)
        colors = ('b', 'm', 'g', 'r', 'k')
    #    linlsqx = np.asarray(x1 + x2 + x3 + x4 +x5)# + np.asarray(x2) + np.asarray(x3) + np.asarray(x4) + np.asarray(x5)
    #    linlsqy = np.asarray(y1 + y2 + y3 + y4 +y5)# + np.asarray(y2) + np.asarray(y3) + np.asarray(y4) + np.asarray(y5)
        groups = ('aircraft general','airframe systems','structure','propellor / rotor','powerplant')
    #    aaa = np.linalg.lstsq(linlsqx, linlsqy)
        
        
        xtot = x1+x2+x3+x4+x5
        ytot = y1+y2+y3+y4+y5
        ztot = z1+z2+z3+z4+z5
        lstsq = []
        for i in range(len(xtot)):
            ab = xtot[i]/ytot[i]
            lstsq.append(ab)
    #    avgavgelay = round(float(sum(lstsq))/len(lstsq),2)
        xttot = np.asarray(xtot)
        yttot = np.asarray(ytot)
        zz = np.polyfit(xttot, yttot, 1)
        zz = list(zz)
        lstx = [zz[:-1],(max(xtot)*zz[0]+zz[:-1])]
        lsty = [0,max(xtot)]
        if year == periodnumber:
            for jk in range(len(xtot)):
                temp12 = []
                temp12.append(xtot[jk])
                temp12.append(ytot[jk])
                temp12.append(ztot[jk])
                output.append(temp12)
        if graph == True:
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
            ax = fig.gca(projection='3d')
            for data, color, group in zip(data, colors, groups):
                x, y, z = data
                ax.scatter(x, y, z, alpha=0.65, c=color, s=10, label=group)
            if year == 7:
                ax.set_xlim(0,500)
            
            
            ax.plot(lsty,lstx, alpha = 0.65, c = 'black')
            #ax.set_ylim(0,30)
            #ax.set_zlim(0,30)
            ax.set_xlabel('total delay')
            ax.set_ylabel('delay frequency')
            ax.set_zlabel('cancellation frequency')#cancellation frequency
            plt.title('3D scatterplot period '+ str(year+1))
            plt.legend(loc=2)
            plt.show()
    return output
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #    import numpy as np
#    import datetime
##    delaylist = []
##    i = 0
##    h = []
#    t = []
##    final = []
#    datelist = []
#    for l in np.arange(timeframe[0]*12, timeframe[1]*12+12,interval):   #overall loop for years. Till put this to 27, since we only have 2016 data until feb or so
#        aa = datetosec(int(np.floor(l/12)),int(l%12)+1,1) # lower limit converted to unix
#        ab = datetosec(int(np.floor((l+interval-1)/12)),int((l+interval-1)%12)+1,31) # upper limit in unix
#        
#        # the lower limit is appended to the array outputting the dates used!
#        # This needs to be kept in mind when evaluatign and drawing conclusions!!!
#        datelist.append(datetime.datetime.fromtimestamp(aa).strftime('%d/%m/%Y')) 
#        
#        
#        #---------------------------------------------------------------------
#        for j in range(1,len(k)):                       #loop for filtering per year 
#            if aa <= k[j][2] < ab:
#                t.append(k[j])
##        c=t[0][3]                                       #need to account for the first line
#        #----------------------------------------------------------------------
#        temp = [t[0][5], t[0][3]]
#        cancel = 0
#        for i in range(len(t)):
#            if t[i][5] == t[i-1][5]:
#                if t[i][4] == 0:
#                    temp.append(t[i][3])
#                if t[i][4] == 1:
#                    cancel += 1
#            if t[i][5] != t[i-1][5]:
#                atadel = [temp[0], sum(temp[1,len(temp)]), len(temp), cancel, (cancel/(len(temp)+cancel))]#pure chaos
#                atadel.append(temp[1:len(temp)])                                #all different delays
#                
#
#
#
#
#
#
#
#
##        for i in range(1,len(t)):
##        
##            if t[i][5] == t[i-1][5]:                    #as long as the ata number is the same as the one befor
##                if t[i][4] == 0:
##                    h.append(t[i][3])                       #statistical stuff
##                    c += t[i][3]                            #adding delaytime
##            if t[i][5] != t[i-1][5]:                    #if a new atanumber is reached
##                j = []                                  #need list to create matrix
##                j.append(t[i-1][5])
##                j.append(c)
##                j.append(h)
##                delaylist.append(j)                     #add [ata,delay]
##                if t[i][4] == 0:
##                    c = t[i][3]                         #reset delay to zero for next ata
##                    h = [t[i][3]]
##                if t[i][4] == 1:
##                    c = 0
##                    h = []
#                  
#        #--------------------------------------------------------------------------
#        delaylist = sorted(delaylist,key=lambda x: x[1] ,reverse=True)
#        
#        final.append(delaylist)
#        t = []
#        delaylist = []
#        
#        
#    return final, datelist
#
#
#def frequency(timeframe, interval, k):
#    import numpy as np
#    import datetime
#    freqlist = []                                       #frequency per time frame
#    t = []                                              #temporary list for storage
#    i=0
#    j=0
#    l=0
#    final = []                                          #
#    datelist = []
#    s=1
#    #s = input("""which column needs to be sorted?"
#    #              1 = Frequency delays
#    #              2 = Frequency cancellations 
#    #              3 = Ratio cancellations over frequency""")
#    
#    for l in np.arange(timeframe[0]*12, timeframe[1]*12+12,interval):   #overall loop for years. Till put this to 27, since we only have 2016 data until feb or so
#        aa = datetosec(int(np.floor(l/12)),int(l%12)+1,1) # lower limit converted to unix
#        ab = datetosec(int(np.floor((l+interval-1)/12)),int((l+interval-1)%12)+1,31) # upper limit in unix
#        
#        # the lower limit is appended to the array outputting the dates used!
#        # This needs to be kept in mind when evaluatign and drawing conclusions!!!
#        datelist.append(datetime.datetime.fromtimestamp(aa).strftime('%d/%m/%Y'))
#        #---------------------------------------------------------------------
#        for j in range(1,len(k)):                       #loop for filtering per year 
#            if aa <= k[j][2] < ab:
#                t.append(k[j])
#        cancel = t[1][4]                                #need to account for the first line
#        c=1                                             #need to account for the first line
#        #----------------------------------------------------------------------
#        for i in range(1,len(t)):                       #loop for the details
#            if t[i][5] == t[i-1][5]:
#                c += 1                                  #frequency increase of 1
#                cancel += t[i][4]                       #number of cancellations
#            if t[i][5] != t[i-1][5]:
#                j = []
#                ratio = round((float(cancel)/c)*100 ,2) #rounding the number (number,digits)
#                j.append(t[i-1][5])                     #making the matrix
#                j.append(c)
#                j.append(cancel)
#                j.append(ratio)
#                freqlist.append(j)
#                c = 1                                   #need to account for the first new
#                cancel = t[i][4]  
#        #--------------------------------------------------------------------------
#        freqlist = sorted(freqlist,key=lambda x: x[s] ,reverse=True)
#        
#        final.append(freqlist)                          #need to accoutn for the first new
#        l += 1
#        t = []
#        freqlist = []
#    return final
#
#def combining(freq, delay):
#    temp_freq = []
#    temp_delay = []
#    combined = []
#    temp1 = []
#    temp2 = []
#    
#    for i in range(len(freq)):                            #sorting loop, for combining delay and frequency, frequency part
#        temp = freq[i]
#        temp = sorted(temp,key=lambda x: x[0])
#        temp_freq.append(temp)
#    
#    for i in range(len(delay)):                            #sorting loop, for combining delay and frequency, delay part
#        temp = delay[i]
#        temp = sorted(temp,key=lambda x: x[0])
#        temp_delay.append(temp)
#    
#    for i in range(len(freq)):
#        for j in range(len(freq[i])):
#            for l in range(len(freq[i][j])):
#                temp1.append(freq[i][j][l])
#            temp1.append(delay[i][j][1])
#            temp1.append(delay[i][j][2])
#            temp2.append(temp1)
#            temp1 = []
#        combined.append(temp2)
#        temp2 = []
#    return combined
#
#
