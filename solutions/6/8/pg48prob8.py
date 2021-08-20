# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:57:00 2020

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 19:33:54 2020

@author: User
"""
# This is the solution to prob:8 of pg 48 from the book SL Loney
import  numpy as np
import matplotlib.pyplot as plt
A = np.array([2,3])
x = np.linspace(-1, 6, 1001)
y1=(4*x-10)/3
y2=(18-3*x)/4
plt.plot(A[0],A[1],'o',label='$A(2,3)$')
plt.text(A[0]*(1-0.5), A[1]*(1), 'A')
plt.plot(x, y1,label='$4x-3y=10$')
plt.plot(x,y2,label='$3x+4y=18$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig('ExVIprob8.pdf')

