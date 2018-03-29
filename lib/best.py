import pickle
import numpy as np


#[[serial][type][date][delay][cancelled][ATA0][ATA1][ATA2][ATA3][ATA4][ATA5]]

"""So we get just a list of delays"""

#=============================================================================
# The following is for delay time. 
#=============================================================================
def arith_mean(data):
    total = 0
    for i in range(len(data)):
        total += data[i]
    arith_mean = float(total)/float(len(data))
    return arith_mean
    
def median(data):
    k = sorted(data)
    if len(data)%2 == 0:
        median = (k[len(data)/2]+k[(len(data)/2)-1])/float(2)
    else:
        idx = int(len(data)/2)
        median = k[idx]
    return median        

def arith_sigma(data):
    some = 0
    for i in range(len(data)):
        some += (data[i] - arith_mean(data))**2
    STD = np.sqrt(some/(len(data)-1))
    return STD
    
def geo_mean(data):
    product = 1
    for i in range(len(data)):
        product *= data[i]
    geo_mean = (product)**(float(1)/(len(data)))
    return geo_mean

def geo_sigma(data):
    some = 0
    for i in range(len(data)):
        some += (np.log((data[i])/float(geo_mean(data))))**2
    above = np.sqrt(float(some)/(len(data)-1))
    geo_STD = (np.e)**above
    return geo_STD


#============================================================================
# Display function
#============================================================================





























































