import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

# Defining the general equation of circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

# Input parameters u and f
#Center of the circle
u = np.array(([11, 2]))
f = 25

# Radius
r = np.sqrt(LA.norm(u)**2-f)

# Generating the circle
circle = circ_gen(u, r)

# Points:
A = np.array(([1, 2]))
B = np.array(([3, -4]))
C = np.array(([5, -6]))
points = np.vstack((A, B, C)).T
labels = ['(1, 2)', '(3, -4)', '(5, -6)']

# Plotting the circle
plt.plot(circle[0,:],circle[1,:],label='$circle$')
plt.scatter(points[0,:], points[1,:])
plt.scatter(u[0], u[1], color = 'red')

# Annotate the points
for i, txt in enumerate(labels):
    plt.annotate(txt, # this is the text
                 (points[0,i], points[1,i]), 
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='left') 
plt.annotate('(11, 2)', (u[0], u[1]), textcoords="offset points", xytext=(0,10), ha='left')

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()