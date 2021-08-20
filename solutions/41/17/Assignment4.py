# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:15:00 2020

@author: Rishab
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	return x_ellipse

#Setting up the Plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-5,5,len)

#Ellipse Parameters
V = np.array(([2,-1],[-1,1]))
u = np.array(([1,-1]))
f = 0
c = -LA.inv(V)@u 
o = [0,0]
c1 = c[np.newaxis,:].T    #Center of Actual Ellipse used in Affine transformation

#Eigenvalues and Eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
pcos = np.cos(np.pi/5.66)
psin = np.sin(np.pi/5.66)
a = np.sqrt((1-f)/D_vec[0])
b = np.sqrt((1-f)/D_vec[1])
xStandardEllipse = ellipse_gen(a,b)


#Major and Minor Axes of the Ellipse
MajorStandard = np.array(([a,0]))
MinorStandard = np.array(([0,b]))

#Affine Transform 
xActualEllipse = P@xStandardEllipse + c1
MajorActual = P@MajorStandard + c1[0]
MinorActual = P@MinorStandard + c1[1]


#Plotting the Standard Ellipse
plt.plot(xStandardEllipse[0,:],xStandardEllipse[1,:],label='Standard Ellipse')

#Plotting the Actual Ellipse
plt.plot(xActualEllipse[0,:],xActualEllipse[1,:],label='Actual Ellipse')


#Labelling the Coordinates
tri_coords = np.vstack((o,c)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['$\mathbf{o}$','$\mathbf{c}$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(1,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.show()
