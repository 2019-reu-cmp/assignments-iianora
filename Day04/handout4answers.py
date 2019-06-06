#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:24:21 2019

@author: isabellaianora
"""
"""
1)Both strings and lists can store information to be acessed for later use. Strings only store leters and lists can store letters as well as numbers. 

2)List comprehensions are useful because they work faster then using append and can do more things.

3)
"""

try:
    import matplotlib as mp
except Exception as e:
    print("matplotlib is not installed!", e)
else:
    #"The else block will excecute if try is successful"
    print('matplotlib version:', mp.__version__ )
    
    """
4)Function that performs dot product using enumerate. Second function using zip.
   """
import math 

A=(1, 2)
B=(3, 4)
dotproduct=0
for a,b in zip(A,B):
    dotproduct +=a*b
print('Dot product is:', dotproduct)

dp=0
for i,x in enumerate(A):
    dp+= B[i]*x
print('dp is:', dp)   