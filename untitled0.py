# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 12:21:19 2018

@author: Laurens
"""

fiblijst = [1,1]
i = 1
n = 0
while n <= 1000000:
    n = fiblijst[i] + fiblijst[i-1]    
    if n <= 1000000:
        fiblijst.append(n)
        i += 1