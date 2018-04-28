# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:44:33 2018

@author: Till
"""

# this is to check the maintenance data base for completeness

import numpy as np
import lib.core as core
import pickle

with open("./Data.txt", "rb") as fp:   # Unpickling list all types
   a = pickle.load(fp) # delay database
   
with open("./DataMaintenance.txt", "rb") as fp:   # Unpickling list all types
   b = pickle.load(fp) # maintenance database


# find distinct plane ids from the maintenance database. 
# this code is shamelessly copied from FleetSizeEstimation.py

years   = range(2011,2015)
actypes = range(1,4)

totalacs   = [] # all acs in the year and type range for the maintenance db
acdatabase = {} # for every year there's a dict of the three types and for each type there is a dict of the serial numbers
for year in years:
    currentyear = {}
    c = core.getbyDate(b, [year,year+1])
    for actype in actypes:
        currentactype = []
        d = core.getbyType(c,actype)
        for entry in d:
            if entry[0] not in totalacs:
                totalacs.append(entry[0])
            if entry[0] not in currentactype:
                currentactype.append(entry[0])
        currentyear[str(actype)] = (currentactype)
    acdatabase[str(year)] = currentyear
    
    
# check which planes appear in both databases
    
# adjust delay database to year range and the airplanes found above in totalacs
delaystripped = core.getbyDate(a, [years[0], years[-1]])
delaystripped = core.getbySerial(delaystripped, totalacs)


commonacs = [] # for acs appearing in both datasets
for line in delaystripped:
    if line[0] not in commonacs:
        commonacs.append(line[0])

# len(totalacs) seems to be 200 in the year range and len(commonacs) seems to be 
# be 171, so I think we are good with this.


## here comes the more important part. Figuring out if all/most of the delay entries
## are actually included in the maintenance data base. This would be a nice lead

print "starting with the long stuff now"

# final lists
delayfinal = core.getbyDate(a, [years[0], years[-1]])
delayfinal = core.getbySerial(delayfinal, commonacs)
maintfinal = core.getbyDate(b, [years[0], years[-1]])
maintfinal = core.getbySerial(maintfinal, commonacs)

threshold = 5 # plus minus days between entries in different lists
# atalevel = 2 # trying with full ata first

commonlines = []

step = 1000
i = 0
for delayline in delayfinal: # runs for like 5 min
    ll = delayline[2] - 86400*threshold # lower limit
    ul = delayline[2] + 86400*threshold # upper limit
    templist = core.getbyTimestamp(maintfinal, [ll,ul])
    ata = delayline[5:]
    ata = ''.join(str(e) for e in ata) # make string from ata number
    #print ata
    templist = core.getbyATA(templist, ata) # populate the rest of the templist, if possible
    #print templist
    if templist:
        commonlines.append(delayline)
    i += 1
    if not i%step:
        print i
    

    
    




