#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import warnings
warnings.filterwarnings("ignore")


# In[15]:


fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 2000
x = np.linspace(-10,10,len)

#Hyperbola parameters
V1 = np.array(([1,-1.5],[-1.5,1]))
u1 = np.array(([5,-5]))
f1 = 21
#Reflection matrix
R1 = np.array(([0,1],[1,0]))
#Eigenvalues and eigenvectors
D_vec1,P1 = LA.eig(V1) 
D1= np.diag(D_vec1)
#Generating the positive hyperbola at the origin
y1 = np.sqrt((1-D_vec1[1]*(x**2))/D_vec1[0])

#Affine transformation parameters
c1 = -LA.inv(V1)@u1 #c=-V^(-1)u
k1 = np.sqrt(np.abs(f1 +u1@c1 ))
#Affine transform 
z1 = np.hstack((np.vstack((x,y1)),np.vstack((x,-y1))))
y_vec1 = k1*P1.T@R1@z1+c1[:,None]


#modified equation values x^TVx-1=0
#Hyperbola parameters
V3 = np.array(([2.5,0],[0,-0.5]))
u3 = np.array(([0,0]))
f3 = 1
#Reflection matrix
R3 = np.array(([0,1],[1,0]))
#Eigenvalues and eigenvectors
D_vec3,P3 = LA.eig(V3)
D3= np.diag(D_vec3)
#Generating the positive hyperbola at the origin
y3 = np.sqrt((1-D_vec3[1]*(x**2))/D_vec3[0])

#Affine transformation parameters
c3 = -LA.inv(V3)@u3 #c=-V^(-1)u
k3 = np.sqrt(np.abs(f3 +u3@c3))
#Affine transform 
z3 = np.hstack((np.vstack((x,y3)),np.vstack((x,-y3))))
y_vec3 = k3*P3.T@R3@z3+c3[:,None]


#centre and modified centre 
xc=[0,-2]
yc=[0,2]

#Plotting

# plotting given hyperbola 

plt.plot(y_vec1[0,0:len],y_vec1[1,0:len], color='b')
plt.plot(y_vec1[0,len:2*len],y_vec1[1,len:2*len], color='b', label = 'Given Hyperbola')


# plotting modified hyperbola

plt.plot(y_vec3[0,0:len],y_vec3[1,0:len], color='orange')
plt.plot(y_vec3[0,len:2*len],y_vec3[1,len:2*len], color='orange', label = 'Modified Hyperbola')

plt.plot(xc[0],yc[0],marker='o',color='black',label='x and y axis with Origin (0,0)') # origin point 
plt.plot(xc[1],yc[1],marker='o',color='red',label='x and y axis with  modified Origin (-2,2)') #origin modified point
# x-y axis with origin (0,0)
plt.axhline(0, color='black')
plt.axvline(0, color='black')

#x-y axis with origin (2,-2)
plt.axhline(2, color='red')
plt.axvline(-2, color='red')


plt.xlabel('$x-axis$');plt.ylabel('$y-axis$')

plt.xlim([-10, 10])
plt.ylim([-10,10])

#annotate centre points 
for x,y in zip(xc, yc):
    label = '   ( %d, %d )' % (x, y)
    ax.text(x, y, label)
    
plt.legend(bbox_to_anchor=(0.8, 1), loc='lower center')
plt.grid()
plt.savefig('hyperbola.png', bbox_inches='tight')
plt.show()


# In[ ]:




