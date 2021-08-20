import numpy as np
#Program to plot  the tangent of a parabola
#Code by GVV Sharma
#Released under GNU GPL
#August 10, 2020

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math


#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *


#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 10000
y = np.linspace(-4,4,len)

#parab parameters
V = np.array(([1,-1],[-1,1]))
u = np.array(([-.5,-.5]))
f = -1
#p = np.array(([1,0]))
#foc = np.abs(p@u)/2

O = np.array(([-.5,-.5]))
#Generating the Standard parabola

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
P[:,[0, 1]] =P[:,[1, 0]]
p = P[:,0]
eta = 2*u@p
foc = -eta/D_vec[0]

x = parab_gen(y,foc)
cA = np.vstack((u+eta*0.5*p,V))
cb = np.vstack((-f,(eta*0.5*p-u).reshape(-1,1)))
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()
print(c,foc)


xStandardparab = np.vstack((x,y))
xActualparab = P@xStandardparab + c[:,np.newaxis]



parab_coords = np.vstack((O,c)).T
##plt.scatter(parab_coords[0,:], parab_coords[1,:])
vert_labels = ['$c (-0.5, -0.5)$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (parab_coords[0,i], parab_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.plot(xActualparab[0,:],xActualparab[1,:],label='Given Parabola',color='r')
plt.plot(c[0],c[1],marker='o',color='black',label='centre (-.5,-.5)') 
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.xlim(-2,10 )
plt.ylim(-2,10)
plt.show()
