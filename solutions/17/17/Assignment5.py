#Assignment 5 : Find  the  equation  of  circle  passing  through  the points (1,1),(2,−1) and (8,2).

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

u = np.array(([9/2,3/2]))
f = 10
r = np.sqrt(LA.norm(u)**2-f)
x_circ= circ_gen(u,r)
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')

plt.annotate("(1, 1)", (1, 1), (1.2, 1))
plt.annotate("(2, -1)", (2, -1), (2.2, -1))
plt.annotate("(8, 2)", (8, 2), (8.2, 2))
plt.annotate("(4.5, 1.5)", (u[0], u[1]), (u[0]+0.2, u[1]))

plt.scatter(1,1,color='blue')
plt.scatter(2,-1,color='blue')
plt.scatter(8,2,color='blue')
plt.scatter(u[0],u[1],color='red')

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()
