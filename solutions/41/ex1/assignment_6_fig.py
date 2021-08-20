import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#Generating points on an ellipse
def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	return x_ellipse

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-5,5,len)

#Ellipse parameters
V = np.array(([14,-2],[-2,11]))
u = np.array(([-22,-29]))
f = -60
c = -LA.inv(V)@u

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
a = np.sqrt(-f/D_vec[0])
b = np.sqrt(-f/D_vec[1])
xStandardEllipse = ellipse_gen(a,b)

print(P)
#Major and Minor Axes
MajorStandard = np.array(([a,0]))
MinorStandard = np.array(([0,b]))

#Affine transform 
xActualEllipse = P@xStandardEllipse
MajorActual = P@MajorStandard
MinorActual = P@MinorStandard

#Plotting the standard ellipse
plt.plot(xStandardEllipse[0,:],xStandardEllipse[1,:],label='Standard ellipse')

#Plotting the actual ellipse
plt.plot(c[0]+xActualEllipse[0,:],c[1]+xActualEllipse[1,:],label='Actual ellipse')

plt.scatter(0,0)
plt.scatter(c[0],c[1])

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
