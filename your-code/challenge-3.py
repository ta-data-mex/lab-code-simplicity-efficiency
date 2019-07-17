#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:47:20 2019

@author: rodolfopardo
"""
#Se realizo una list comprehension para los for anidados 
#Se realiza un anidado correcto ya que habian numeros que no eran relevantes 



def my_function(X):
    solutions = [[x,y,z] for x in range(X) for y in range(x) for z in range(y) if (x*x==y*y+z*z)]
    m = 0
    for solution in solutions:
        if m < max(solution):
            m = max(solution)
    return m

X = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " + str(my_function(int(X))))

