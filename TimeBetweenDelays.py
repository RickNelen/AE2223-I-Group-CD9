# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 23:52:57 2018

@author: Till
"""

import numpy as np
import time
import datetime
import matplotlib.pyplot as plt
import lib.core as core
import pickle

# Read the csv and generate the Data.txt pickle
#import FunctionLibrary.genPickle

# import the delay pickle
with open("./Data.txt", "rb") as fp:   # Unpickling list all types
   b = pickle.load(fp)

# convert to numpy matrix 
b = np.array(b)


""" First: figure out some plane stats. """
# p is array with [id,type,first apperance (UNIX time), total # of incedents, avg relative number of incidence per year (to assumed age at 01/Feb/2016 (end of dataset))]

reftime = time.mktime(datetime.datetime.strptime("01/02/2016", "%d/%m/%Y").timetuple()) # 1 feb 2016 in UNIX time

ids = set(b[:,0]) # get all different ids in one array
p = np.zeros([len(ids),5]) # initialize p with the correct dimensions

i = 0
for idint in ids:
    p[i,0] = idint # identifyer
    firstrow = b[np.where(b[:,0] == idint)[0][0],:] # row of first appearance of a/c id
    p[i,1] = firstrow[1] # type
    p[i,2] = firstrow[2] # first appearance
    p[i,3] = len(np.where(b[:,0] == idint)[0]) # total number of incidents
    p[i,4] = float(p[i,3]) / ((reftime - p[i,2])/(3600.0*24*365)) # relative number of incidents
    i += 1
    
"""
# get a/c id with highest failure rate: np.argmax(p, axis=0) gives a vector with the indices of the maxima for each column in the dataset (axis=1 would be for each row)
highestid  = p[np.argmax(p, axis=0)[4],0]
highestval = p[np.argmax(p, axis=0)[4],4]
"""

"""
# plot aircraft assumed current age against relative number of incidents
x = (reftime - p[:,2])/(3600.0*24*365)
y = p[:,4]
fig, ax = plt.subplots()
ax.scatter(x, y)
plt.show
"""



""" Second: For plane with most delay incidents (id 11257, 809 incidents), for each ata chapter involved, get list of tfb (time between failure) """
subset = np.concatenate((np.array(core.getbySerial (b, 11257)),  np.zeros( [len( np.array( core.getbySerial (b, 11257) ) ), 1]) ), axis=1) # also add a column of zeros here
subset[:,-1] = subset[:,-7]*10 + subset[:,-6]

atas = list(set(subset[:,-1])) # list of distinct ata numbers
atas2 = [] # the ata numbers that have more than 1 failure

tbf = [] # holds time between failures for each ata number
for ata in atas:
    if len(np.array(core.getbyATA (subset, int(ata)))) > 1:
        tbf.append(np.diff(np.array(core.getbyATA (subset, int(ata)))[:,2]) / (24.*3600))
        atas2.append(ata)

"""
# find ATA with most occurences; useless, since it is always 0 in the data...
lengths = []
for line in tbf:
    lengths.append(len(line))
    
idval, value = max(enumerate(lengths), key=operator.itemgetter(1))
"""

#component = 11 # component in atas list
hist = []
for component in range(0,len(atas2)):
    print atas2[component]
    
    """
    x = np.arange(1,len(tbf[component])+1)
    y = tbf[component]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    plt.show
    """
    # histogram with bins 0-10, 10-20 etc until 100
    hist.append(np.histogram(tbf[component], bins=np.arange(0,30,3), range=(0.,100.)) )
    #fig, ax = plt.subplots()
    #ax.bar(hist[component][1][0:-1],hist[component][0],width=3)
    #plt.show

# ToDo: Check with more planes/ATAs, that often the TBF is almost zeros or rather large never in between
# fit some sort of bi-modal distribution through some (find out what "some" means in the context). Find out how to come of with a confidence bound until
# which we are sure that the small tbf is actually due to "double failure"





