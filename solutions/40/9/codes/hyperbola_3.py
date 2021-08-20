#Program to plot  the tangent of a hyperbola
#Code by GVV Sharma
#Released under GNU GPL
#August 9, 2020

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

from conics.funcs import *

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-2,2,len)

def hyper_gen(y):
	x = np.sqrt(1+y**2)
	return x

#hyper parameters
V = np.array(([55,-60],[-60,20]))
u = np.array(([32,-24]))
f = 0
Vinv = LA.inv(V)
#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
#print(D,P)
uconst = u.T@Vinv@u-f
a = np.sqrt(np.abs(uconst/D_vec[0]))
b = np.sqrt(np.abs(uconst/D_vec[1]))
print(a,b)
#Generating the Standard Hyperbola
x = hyper_gen(y)
xStandardHyperLeft = np.vstack((-x,y))
xStandardHyperRight = np.vstack((x,y))

#Affine Parameters
c = -Vinv@u
print(c)
R =  np.array(([0,1],[1,0]))
ParamMatrix = np.array(([a,0],[0,b]))


#Generating the actual hyperbola
xActualHyperLeft = P@ParamMatrix@R@xStandardHyperLeft+c[:,np.newaxis]
xActualHyperRight = P@ParamMatrix@R@xStandardHyperRight+c[:,np.newaxis]


#Hyperbola vertices
V1old = np.array([1,0])
V2old = -V1old

V1 = P@R@ParamMatrix@V1old+c
V2 = P@R@ParamMatrix@V2old+c



##Major and Minor Axes
MajorStandard = np.array(([a,0]))
MinorStandard = np.array(([0,b]))

#
##Plotting the standard hyperbola
plt.plot(xStandardHyperLeft[0,:],xStandardHyperLeft[1,:],label='Standard hyperbola',color='b')
plt.plot(xStandardHyperRight[0,:],xStandardHyperRight[1,:],color='b')

#Center
xc=[-0.32]
yc=[0.24]


#Plotting the actual hyperbola
plt.plot(xActualHyperLeft[0,:],xActualHyperLeft[1,:],label='Actual hyperbola',color='r')
plt.plot(xActualHyperRight[0,:],xActualHyperRight[1,:],color='r')

plt.plot(xc[0],yc[0],marker='o',color='black',label='centre (-0.32,0.24)') # origin point 
#
plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

# x-y axis with origin (0,0)
plt.axhline(0, color='black')
plt.axvline(0, color='black')


plt.show()
