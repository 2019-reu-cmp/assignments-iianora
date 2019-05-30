#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:36:50 2019

@author: isabellaianora
"""

"""1)As your tolerance gets smaller, the number of iterations increase. For a tolerance of 10e-3 you get 7 iterations. For a tolerance of 10e-6 you get 17 iterations and for a tolerance of 10e-9 you get 27 iterations. I think this happens because as you decrease the tolerance, the interval over which the calculations are being done is smaller so to get more accurate answers, the program is breaking down the function into smaller pieces giving you more iterations. 

2)You can make bisection.py a function of its own with its imputs being a function and tolerance so that all you have to do is change the input and then you can run it quicker.

3)Tuples are fixed, you can't add anything to them and they are not allowed to have repeating elements. They can be used when an immutable sequence of homogeneous data is being used. Lists can be appended and can have repeated elements. They are typically used when homogeneous items are being used. Dictionaries are ways of defining variables, you cannot use the same variable within a dictionary. A set is an unordered collection of distinct hashable objects. It can be used to remove duplicates from a sequence.

4)You can use an if statement to say if variable is list, print('list') elif print('this is not a list')
