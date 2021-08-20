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

# Defining equation of a line - for the tangent
def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

# Input parameters u and f
# Center of the circle
u = np.array(([0, 0]))
f = -4

# Radius:
r = np.sqrt(LA.norm(u)**2-f)

# Generating the circle
circle = circ_gen(u, r)

# Generating the tangents
Q1 = np.array(np.sqrt([4/5, 16/5]))
Q2 = np.array(-np.sqrt([4/5, 16/5]))
Q = np.vstack((Q1, Q2)).T
labels = ['(0.894, 1.788)', '(-0.894, -1.788)']
original = np.array(([3, 1.5]))
m = np.array(([1, -0.5]))
k1 = 2
k2 = -2

#Generating all lines
x_AB = line_dir_pt(m, Q1, k1, k2)
x_BC = line_dir_pt(m, Q2, k1, k2)
l = line_dir_pt(m,original, 1, -1)

# Plotting the circle
plt.plot(circle[0,:],circle[1,:],label='$circle$')

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$Tangent1$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$Tangent2$')
plt.plot(l[0,:],l[1,:],label='$x+2y = 6$')

# Annotate pts:
plt.scatter(u[0],u[1],color='red')
plt.scatter(Q[0,:], Q[1,:])
plt.annotate("(0, 0)", (u[0], u[1]), (u[0]+0.1, u[1]))

for i, txt in enumerate(labels):
    plt.annotate(txt, # this is the text
                 (Q[0,i], Q[1,i]), 
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center') 


# Labelling the figure
plt.xlabel('$x axis$')
plt.ylabel('$y axis$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()