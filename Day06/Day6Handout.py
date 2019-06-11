#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:29:50 2019

@author: isabellaianora
"""
import numpy as np
import math

"""
1)Implement a function integration using the trapezoid rule
"""
def f(x, a=1):
    return a*x**2

xs= np.arange(10)
ys= f(xs)

print(ys)

dx=1
trap = dx * (f(xs + dx) + f(xs)) / 2

print(trap)

"""
2)Integrate using Simpson rule
"""
#a= xs[0]
#b= xs[-1]
#
#h = (b - a) / 3
#factor = (f(a) +
#          3*f((2*a + b) / 3) +
#          3*f((a + 2*b) / 3) +
#          f(b))
#integral = (3 * h / 8) * factor
#
#print(integral)


"""
3)Root finder using Newton's method
"""
def f_derivative(x, a=1):
    return 2*a*x


#for n in range(-5,5):
#    z = xs[n]- f(xs[n])/f_derivative(xs[n])
#    print(z)

guess1=1

#guess2= guess1- f(guess1)/f_derivative(guess1)
#
#print(guess2)
#print(guess1-guess2)
#
#guess3= guess2- f(guess2)/f_derivative(guess2)
#print(guess3)


guess1=1
tolerance= 0.001
guess2= guess1- f(guess1)/f_derivative(guess1)
difference=guess1- guess2
#print(difference)


while difference> tolerance:
    guess2= guess1- f(guess1)/f_derivative(guess1)
    difference=guess1- guess2
    #print(difference)
    guess1=guess2
    #print(guess2)

    

  
   

#x1 = x0 - f(x0)/df(x0)




"""
4)Root finder using secant method
"""
x0= 1
x1= 2
x2= x1 - f(x1) * (x1 - x0)/(f(x1) - f(x0))


while (difference> tolerance):
    x2 = x1 - f(x1) * (x1 - x0)/( f(x1) - f(x0) )
    difference= x2-x1
    print(difference)
    x1=x2
    x0=x1
    print(x2)





     
     
     