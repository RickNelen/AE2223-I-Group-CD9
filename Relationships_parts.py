# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:17:44 2018

@author: Laurens
"""

#Tijd tot failure
#Verwachte delay
#Kans cancellation als het faalt
#per aircraft values
import matplotlib.pyplot as plt
import lib.core as core

interval = 36
k = core.unpickle("./Data.txt")                                                 #getting the data ready
k = core.sortata(k, 3)
final, date = core.getdelaylist([1988,2015],interval,k) 


final_delay = []
final_rel_year = []
final_rel_allyears = []
temp_rel = []
temp2_rel = []
final2_rel_allyears = []
#----------------------------------------------------------------------------------------actual program starts
for i in range(len(final)):                                     #relation loop
    for j in range(len(final[i])):
        if final[i][j][2] != 0:
            a = int(round(float((float(interval)/12)*365/final[i][j][2]),0))                  #amount of days average delay
            b = round(float(final[i][j][1])/ final[i][j][2],0)                          #average delay
        if final[i][j][2] == 0:
            a = int(round(float((float(interval)/12)*365/final[i][j][3]),0))
            b = 0
        b = int(b)
        c = final[i][j][4]                                      #cancellation ratio
        temp_rel.append(final[i][j][0])
        temp_rel.append(a)
        temp_rel.append(b)
        temp_rel.append(c)
        temp2_rel.append(temp_rel)
        final_rel_allyears.append(temp_rel)
        temp_rel = []
    final_rel_year.append(temp2_rel)
    temp2_rel = []


#--------------------------------------------------------------------------------------combining the same atanumber lines
#USED FOR THE ALL YEARS COMBINED LIST
final_rel_allyears = sorted(final_rel_allyears,key=lambda x: x[0])
j = []
d = round(float((float(interval)/12)*365)/final_rel_allyears[0][1],0)
e = final_rel_allyears[0][2]
f = final_rel_allyears[0][3]
g = 1
for i in range(1, len(final_rel_allyears)):
    if final_rel_allyears[i][0] == final_rel_allyears[i-1][0]:                    #as long as the ata number is the same as the one befor
        if final_rel_allyears[i][1] != 0:
            d += round(float((interval/12)*365)/final_rel_allyears[i][1],0)                              #adding
        e += final_rel_allyears[i][2]                                               #adding
        f += final_rel_allyears[i][3] 
        g += 1                                               #adding
    if final_rel_allyears[i][0] != final_rel_allyears[i-1][0]:                    #if a new atanumber is reached
        j.append(final_rel_allyears[i-1][0])
        if d != 0:
            j.append(int(round((28*365)/d,0)))
        if d == 0:
            j.append(28*365)
        j.append((e/g))
        j.append(round(f/g,2))
        final2_rel_allyears.append(j)
        j = []
        g = 1
        if final_rel_allyears[i][1] != 0:
            d = round(float((float(interval)/12)*365)/final_rel_allyears[i][1],0)
        if final_rel_allyears[i][1] == 0:
            d = float((float(interval)/12)*365)
        e = final_rel_allyears[i][2]
        f = final_rel_allyears[i][3]



#------------------------------------------------------------------------------------------SCATTERPLOT
x = []
y = []
xfinal = []
yfinal = []
top10 = [732, 275, 612, 291, 324, 323, 342, 302, 273, 771]
colours = []

for i in range(len(final2_rel_allyears)):                                       #x-axis
#    if final2_rel_allyears[i][0] in top10:                                         #highlighting top10
#        xfinal.append(final2_rel_allyears[i][1])
#    else:                                                                       #the rest
        x.append(final2_rel_allyears[i][1])
#for i in range(len(x)):
#    xfinal.append(x[i])                                                         #first ten values top 10 for colour coding

for i in range(len(final2_rel_allyears)):                                       #y-axis, same way as above.
#    if final2_rel_allyears[i][0] in top10:
#        yfinal.append(final2_rel_allyears[i][2])
#    else:
        y.append(final2_rel_allyears[i][2])
#for i in range(len(y)):
#    yfinal.append(y[i])
for i in range(len(final2_rel_allyears)):                                       #colours
    if float(y[i])/x[i] >= 1.:
        colours.append('red')
    if 1. > float(y[i])/x[i] >= 0.1:
        colours.append('orange')
    if 0.1 > float(y[i])/x[i]:
        colours.append('green')

#--------------------------------------------------------------------------------------diaganol lines
area = 15
plt.scatter(x, y ,c=colours,  s=area, alpha=0.8)

x1 = [1,20000]                                                                  #lines in the graph
y1 = [1,20000]
x2 = [1,20000]
y2 = [0.1,2000]
plt.plot(x1 , y1, c = 'black', alpha = 0.3)
plt.plot(x2 , y2, c = 'black', alpha = 0.3)

plt.show()