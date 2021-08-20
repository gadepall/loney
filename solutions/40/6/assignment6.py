#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 01:21:16 2020

@author: shantanu
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/home/shantanu/mtech/la/py_codes/CordGeo')        #path to my scripts


#local imports
from conics.funcs import *


#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-2,2,len)

#hyper parameters
V = np.array(([3,-4],[-4,-3]))
u = np.array(([5,-13/2]))
f = 8
Vinv = LA.inv(V)
#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
#print(D,P)
uconst = u.T@Vinv@u-f
a = np.sqrt(np.abs(uconst/D_vec[0]))
b = np.sqrt(np.abs(uconst/D_vec[1]))
#print(a,b)
#Generating the Standard Hyperbola
x = hyper_gen(y)
xStandardHyperLeft = np.vstack((-x,y))
xStandardHyperRight = np.vstack((x,y))

#Affine Parameters
c = -Vinv@u
#print(c)

R =  np.array(([0,1],[1,0]))
ParamMatrix = np.array(([a,0],[0,b]))

#Generating the eigen hyperbola
xeigenHyperLeft = R@ParamMatrix@xStandardHyperLeft
xeigenHyperRight = R@ParamMatrix@xStandardHyperRight

#Generating the actual hyperbola
xActualHyperLeft = P@ParamMatrix@R@xStandardHyperLeft+c[:,np.newaxis]
xActualHyperRight = P@ParamMatrix@R@xStandardHyperRight+c[:,np.newaxis]


#Hyperbola vertices
V1old = np.array([1,0])
V2old = -V1old

V1 = P@R@ParamMatrix@V1old+c
V2 = P@R@ParamMatrix@V2old+c

#print(V1)
#print(V2)
#Plotting the actual hyperbola
plt.plot(xActualHyperLeft[0,:],xActualHyperLeft[1,:],label='hyperbola',color='r')
plt.plot(xActualHyperRight[0,:],xActualHyperRight[1,:],color='r')
#

plt.plot(c[0],c[1],'o-')
plt.plot(V1[0],V1[1],'o-')
plt.plot(V2[0],V2[1],'o-')
plt.annotate(" Centre (-1.64,0.02)",(c[0],c[1]));
plt.annotate(" Vertex 1 \n (-1.525,0.25)",(V1[0],V1[1]));
plt.annotate(" Vertex 2 \n (-1.75,-0.21)",(V2[0],V2[1]));
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
