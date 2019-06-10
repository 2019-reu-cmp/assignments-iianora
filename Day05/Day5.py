#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:39:38 2019

@author: isabellaianora
"""

import numpy as np
import matplotlib.pyplot as plt 

months, sunspots = np.loadtxt('sunspots.tsv', unpack=True)


plt.plot(months,sunspots)
plt.xlabel('Months')
plt.ylabel('Sunspots')
plt.show()


plt.scatter(months,sunspots)
plt.xlabel('Months')
plt.ylabel('Sunspots')
plt.show()



N=3143
window_1st= [5]
avg=np.zeros((len(window_1st), N))
for i, window in enumerate(window_1st):
    avg2=np.ones(window)/window
    avg[i, :]= np.convolve(sunspots,avg2, 'same')

plt.plot(months, avg[i, :] + (i+1)*50, label=window)
plt.xlabel('Months')
plt.ylabel('Sunspots')
plt.show()