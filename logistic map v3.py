# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:04:48 2022

@author: cjfau
"""


import numpy as np
import matplotlib.pyplot as plt

def limit_points(r, n=1, x0=0.5):
    
    def logistic(x):
        y = r*x*(1-x)
        return y
    
    f = logistic
    
    terms = []
    for i in range(0,10):
        y = f(x0)
        terms.append(y)
        x0 = y
    
    return terms

parameter = np.linspace(3, 4, 500)

x=[]
y=[]
for i in parameter:
    codomain = limit_points(i)
    for j in codomain:
        x.append(i)
        y.append(j)
        
plt.scatter(x,y, marker = '.')