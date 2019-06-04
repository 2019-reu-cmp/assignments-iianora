#!/usr/bin/env python3
""" pi.py - 
"""
import math


def srinivasa(k):
    
    i=0
    calc=0
    coff=2*math.sqrt(2)/9801
    while i<k:
        calc+=(math.factorial(4*i)*(1103+26390*i))/(((math.factorial(i))**4)*396**(4*i))
        i+=1
        print(i)
        
        calc_pi=1/(coff*calc)   
    return calc_pi, math.pi-calc_pi
    

if __name__ == '__main__':
    iterations = 3
    print(srinivasa(iterations))