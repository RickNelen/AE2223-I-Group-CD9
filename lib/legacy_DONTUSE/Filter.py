#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:28:14 2018

--> filters by year by coverting the unix time to a year string ('%Y')

@author: Misa
"""

#Data
 
#[[serial][type][date][delay][cancelled][ata1][ata2][ata3][ata4][ata5][ata6]]
 


import pickle
import datetime
import time

with open("../../Data.txt", "rb") as fp:   # Unpickling
   b = pickle.load(fp)

"""
st = []
for i in range(len(b)):
    year = datetime.datetime.fromtimestamp(int(b[i][2])).strftime('%Y')
    st.append(year)
"""
"""
first_year = 1987
step = 1
h = 0
k = 0
for k in range(0,15):
    for j in range(len(st)):
        if first_year <= st[j] < first_year + step:
        #    h = j
            print j
        else:
            break
    k += 1
        
"""
#"""

# Answer Beginning of Year to End of Year

year0 = int(datetime.datetime.fromtimestamp(int(b[1][2])).strftime('%Y'))
print "Beginning of year: "+ str(year0)
yearn = int(datetime.datetime.fromtimestamp(int(b[-1][2])).strftime('%Y'))
print "Latest Year: " + str(yearn)
n = yearn - year0 + 1
print "number of years: ", n

#Extracting List from b
def extract(b, year0, year1):
    lst = []
    k = 0
    date0 = "01/01/"+str(year0)
    date1 = "01/01/"+str(year1)
    unix0 = time.mktime(datetime.datetime.strptime(date0, "%d/%m/%Y").timetuple())
    unix1 = time.mktime(datetime.datetime.strptime(date1, "%d/%m/%Y").timetuple())
    while k < len(b):
        if int(unix0) < b[k][2] < int(unix1):
            lst.append(b[k])
            k += 1
        else:
            k += 1
    return lst


#Creating List Within Library
Step_size = 3 #<------ To edit must be factor of 30 bitch
obj = {}
i = 0

while i < n/Step_size:
    year1 = year0 + Step_size
    value = extract(b, year0, year1)
    obj[str(year0)] = value
    i+=1
    year0 = year0 + Step_size

#
for key in obj.keys():
    info = list(obj.values())
    print info[0]
#"""
#with open("./Data.txt", "wb+") as fp:   #Pickling
#   pickle.dump(k, fp)


