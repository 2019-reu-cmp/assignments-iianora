#!/usr/bin/env python3
"""fitting.py -- fits a two overlapping Gaussian peaks

Starting Code:
Mike Moran
mmoran0032@gmail.com
2016-06-28
Benjamin Rose
benjamin.rose@me.com
2017-06-20
Chris Seymour
seymour.16@nd.edu
2019-06-18
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import statistics as stat



def gaus(x, A, mu, sigma):
    """
    Returns y-value, for each given x, making a Gaussian.

    Parameters
    ----------
    x : numpy.array
        The input values for the Gaussian function. Similar to the x values 
        used in a plotting command.

    A : float
        Maximum value of the Gaussian.

    mu : float
        Location (along x-axis) for the center of the Gaussian. Maybe outside 
        the range of `x`.

    sigma : float
        Width of the Gaussian.

    Return
    ------
    numpy.array
        A y-value (in a Gaussian shape) for each `x` given.
    """
    return A * np.exp(-(x - mu)**2/(2 * sigma**2))


def fitter(x, A0, mu0, sigma0, A1, mu1, sigma1):
    """
    Function to fit to the data. Two Gaussians that... 
    """
    
    global G1
    global G2
    G1= A0 * np.exp(-(x - mu0)**2/(2 * sigma0**2)) 
    G2= A1 * np.exp(-(x - mu1)**2/(2 * sigma1**2))
    G_tot= G1+G2
    return G_tot



bins, counts = np.loadtxt('two_peaks.txt', unpack=True)
x= np.linspace(0, 30, 100)
A= np.max(counts)
mu= stat.mean(x)
sigma= stat.stdev(x)



paras, _ = curve_fit(fitter, bins, counts)



plt.scatter(bins, counts)
plt.plot(x, fitter(x, *paras))
plt.plot(x, G1)
plt.plot(x, G2)


plt.show()



#pars, _ = curve_fit(gaus, bins, counts)
#
#plt.scatter(bins, counts)
#plt.plot(x, gaus(bins, *pars))
#plt.show()  


#Z = curve_fit() # fitting method
 
 
 
 
 



#import matplotlib.pyplot as plt
#import numpy
#from scipy.optimize import curve_fit
#
#x = numpy.linspace(0, 10)
#y = 2 * x + 2 *numpy.random.rand(50) - 1  # just to get scatter
#
#def lin(x, m, b):
#    return m * x + b
#
#pars, _ = curve_fit(lin, x, y, p0=[1., 0.])
#
#plt.scatter(x, y)
#plt.plot(x, lin(x, *pars))
#plt.show()