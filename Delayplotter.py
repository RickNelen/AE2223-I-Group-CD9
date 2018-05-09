# -*- coding: utf-8 -*-
"""
Created on Tue May 08 14:25:16 2018

@author: Rick
"""


import lib.core as core
import plotly
import plotly.graph_objs as go
import numpy as np

plotly.tools.set_credentials_file(username='rnelen', api_key='hF9AVF1jzXS8MDvhXkMq')
#input
#[aircraft type, ATA, [years]]

def delayplotter(aircrafttype, ATA, begin,end,interval):                        # interval in months
    k = core.unpickle("./Data.txt")  
    k = core.getbyType(k,aircrafttype)                                          #getting the data ready
    k = core.sortata(k, 2)
    delay, date = core.getdelaylist([begin,end],interval,k)
    
    newdate = []
    newdelay = []
    years = []
    final = []
    mini = []
    maxi = []
    
    for i in range(len(delay)):
        for j in range(len(delay[i])):
            for l in range(len(ATA)):
                if delay[i][j][0] == ATA[l]:
                    newdate.append(date[i])
                    newdelay.append(delay[i][j])
                    
    for x in range(len(newdate)):
        year = newdate[x]
        year = year[-4:]
        years.append(year)
        
        average = round(float(newdelay[x][1])/float(newdelay[x][2]),2)
        minimum = min(newdelay[x][5])
        maximum = max(newdelay[x][5])
        newdelay[x].append(average)
        newdelay[x].append(minimum)
        newdelay[x].append(maximum)
       # print newdelay[x]
                             
  # now we create a list with [ata, total delay, delay freq., average delay, min delay, max delay]
        del newdelay[x][3] 
        del newdelay[x][3] 
        del newdelay[x][3]
   # print newdelay
        
    for z in range(len(newdate)):
        final.append(newdelay[z][3])
        mini.append(newdelay[z][4])
        maxi.append(newdelay[z][5])
            
   # print final            
    final = np.array(final)
    mini = np.array(mini)
    maxi = np.array(maxi)
        
    return years,final,mini,maxi



years, final, mini,maxi = delayplotter(2,[32],1988,2015,12)
data = [
    go.Scatter(
        x = years,
        y = final,
        error_y=dict(
            type='data',
            symmetric=False,
            array=maxi - final,
            arrayminus=final - mini
        )
    )
]
plotly.plotly.iplot(data, filename='ATA32')


years, final, mini,maxi = delayplotter(2,[27],1988,2015,12)
data = [
    go.Scatter(
        x = years,
        y = final,
        error_y=dict(
            type='data',
            symmetric=False,
            array=maxi - final,
            arrayminus=final - mini
        )
    )
]
plotly.plotly.iplot(data, filename='ATA27')
