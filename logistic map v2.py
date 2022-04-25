# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 16:59:32 2022

@author: cjfau
"""


import numpy as np
import matplotlib.pyplot as plt
import random as rand

lam = 3.55 #parameter for logistic map, used for plots 1 & 2, higher periods appear for higher parameter value

def logistic(x): #basic function for logistic map, used for plots 1 & 2
    y = lam*x*(1-x)
    return y

def compose(f, g): #composition of 2 functions
    return lambda x: f(g(x))

def recursive_compose(f, n): #able to compose a function with itself repeatedly
    g = f                    #equivalent to f^n(x)
    for i in range(1,n):
        g = compose(g, f)
    return g

def my_fixed_point(f): #the zeroes of the new function are the fixed points of the input function
    return lambda x: f(x) - x

def periodic_point(n, r): #finds periodic points of period n at value of parameter r
    
    def logistic_loop(x): #this block composes the function with itself n times, then applies my_fixed_point
        y = r*x*(1-x)     #the zeroes of this function will be the period n points
        return y
    f = recursive_compose(logistic_loop, n)
    f = my_fixed_point(f)
    
    test_x = np.linspace(0, 1, 1000) #divides the domain into many pieces, then finds where the value of the function
    a = f(test_x[1])                 #changes sign, these are the zeroes
    bracket_list = []
    for i in test_x[1:len(test_x)]:
        y = f(i)
        if y/a < 0:
            a = y
            bracket_list.append(i)
    return bracket_list #ordered list of fixed points
    

logistic2 = compose(logistic, logistic) #self compositions, used for plots 1 & 2
logistic4 = compose(logistic2, logistic2)

plt.figure(1)            #turns fixed points into zeroes
x = np.linspace(0,1,500) 
plt.plot(x, logistic(x)-x, label = 'Period 1')
plt.plot(x, logistic2(x)-x, label = 'Period 2')
plt.plot(x, logistic4(x)-x, label = 'Period 4')
plt.legend()
plt.ylim(-1, 1)
plt.xlim(0, 1)
plt.hlines(0,0,1, color='red')

plt.figure(2)               #plots logistic map and self-compositions
x = np.linspace(0,1,500)    #intersections with y=x are periodic points
plt.plot(x, logistic(x), label = 'Period 1')
plt.plot(x, logistic2(x), label = 'Period 2')
plt.plot(x, logistic4(x), label = 'Period 4')
plt.plot(x, x)
plt.legend()
plt.ylim(0, 1)
plt.xlim(0, 1)


def bifurcation(n, xmin=0, xmax=4, iterations = 2000): #parses many different values of parameter, 
    x = []                                             #then identifies periodic points/limit points
    y = []                                             #using periodic_points
    domain = np.linspace(xmin, xmax, iterations)
    for i in domain:
        codomain = periodic_point(n, i) #creating every ordered pair, multiple y's for each x
        for j in codomain:
            x.append(i)
            y.append(j)
    return plt.scatter(x, y, marker = '.', label = 'Period ' + str(n))
            
plt.figure(3) #plotting  bifurcation diagram

for i in [8,4,2,1]: #layering multiple periods on top of each other
    bifurcation(i)  #each period will contain the points of its factors, put lowest period on top
    
plt.legend()

def cobweb(x0=0, r=0, iterations=100, ymin=0, ymax=1, xmin=0, xmax=1): #cobwebs logistic function
    if x0 == 0:
        x0 = rand.random()      #if starting point and parameter not specified, randomly chosen in a range
    if r == 0:                  #with a single fixed point
        r = rand.uniform(1,3)   #periodic points appear for r>3
    
    def logistic_cobweb(x):
        y = r*x*(1-x)
        return y
    
    #f = logistic_cobweb
    f = np.cos
    
    fig = plt.figure()
    domain = np.linspace(xmin,xmax,500)
    plt.plot(domain, f(domain))
    plt.plot(domain, domain)
    plt.ylim(ymin, ymax)
    plt.xlim(xmin, xmax)
    
    per_set = periodic_point(4, r) #labeling periodic points to better show convergence
    for i in per_set:
        plt.axvline(x=i, ymin=0, ymax=logistic_cobweb(i), color = 'black')
    
    y1 = 0
    for i in range(0, iterations): #drawing lines for cobwebs
        y2 = f(x0)
        plt.axvline(x=x0, color='g', ymin=y1, ymax=y2)
        plt.hlines(y2, x0, y2, color='g')
        x0 = y2
        y1 = y2
    
    return fig

cobweb()











