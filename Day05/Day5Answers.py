#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:26:44 2019

@author: isabellaianora
"""

"""

1)You should use arrays instead of lists for numbers because numpy is better to work with, it allows you to do more math with the array.

2)Explore basic math operations on vectors
"""
import numpy as np

a=np.array([0, 1, 2])
b=np.arange(3)
c=np.linspace(0, 2, 3)

#print (a+b+c)
#print(a*b*c)
"""
The math operation will be applied to the same spot in each vector and then will be put into a new vector. For example when I multiply a and b a[1] will be multiplied by b[1] and then that value will be stored in some new vector in the 1 position.

3)To use statistic functions in multidimentional arrays, you must specify which dimention you want the funciton to apply to. 

"""
#print(a.mean(axis=0))

"""
4)Histogram
"""
import matplotlib.pyplot as plt
months, number = np.loadtxt('sunspots.tsv', unpack=True)

plt.hist(number, bins=50)
plt.xlabel('Sunspots in a month')
plt.ylabel('Months with that number of spots')
plt.title('Sunspot Number Distibution')
plt.show()