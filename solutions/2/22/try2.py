# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:45:05 2020

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:46:45 2020

@author: User
"""

import  numpy as np
import matplotlib.pyplot as plt

# A,B and C are the vertices of the triangle whose coordinates are the inputs
A = np.array([0,0])
B = np.array([3,3])
C = np.array([6,0])
# l,m and k are also inputs which are defined as below
# for AD:DB=l:k
# for DE:EC=m:l+k
l=1 
m=1
k=1
# for showing the inputs
print('A coordinates are',A)
print('B coordinates are',B)
print('C coordinates are',C)
# initializing D  and E which are yet to be determined
D=np.zeros(2)
E=np.zeros(2)

# Coordinates of D and E are determined here
#D[0]=l/(l+k)*B[0]+(k/(l+k))*A[0]
#D[1]=l/(l+k)*B[1]+(k/(l+k))*A[1]
D=(l*B+k*A)/(l+k)
E=(m*C+(l+k)*D)/(m+l+k)

#E[0]=m/(m+l+k)*C[0]+(l+k)/(m+l+k)*D[0]
#E[1]=m/(m+l+k)*C[1]+(l+k)/(m+l+k)*D[1]

# line_gen is a function which generates 20 points between the two specified end points 

def line_gen(AA,BB):
	len = 20
	dim = AA.shape[0]
	x_AB = np.zeros((dim,len))
	lam_1 = np.linspace(0,1,len)
	for i in range(len):
		temp1 = AA + lam_1[i]*(BB-AA)
		x_AB[:,i]=temp1.T
	return x_AB

#generating lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA=line_gen(C,A)
x_DE=line_gen(D,E)
x_EC=line_gen(E,C)
#

#plotting the all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_EC[0,:],x_EC[1,:],label='$EC$')

#plotting the points with text and dot
plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1-0.5), A[1]*(1), 'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1-0.1), B[1]*(1), 'B')
plt.plot(C[0],C[1],'o')
plt.text(C[0]*(1-0.1), C[1]*(1), 'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0]*(1-0.1), D[1]*(1), 'D')
plt.plot(E[0],E[1],'o')
plt.text(E[0]*(1-0.1), E[1]*(1+0.2), 'E')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
#plt.show()
# saving the figure in pdf format
plt.savefig('Ex1prob22.pdf')

