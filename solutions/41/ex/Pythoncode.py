import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
	
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-5,5,len)

V = np.array(([35,-6],[-6,30]))
u = np.array(([16,-54]))
f = 39
c = -LA.inv(V)@u

D_vec,P = LA.eig(V)
D = np.diag(D_vec)
a = np.sqrt(f/D_vec[0])
b = np.sqrt(f/D_vec[1])

len = 50
theta = np.linspace(0,2*np.pi,len)
x_ellipse = np.zeros((2,len))
x_ellipse[0,:] = a*np.cos(theta)
x_ellipse[1,:] = b*np.sin(theta)
	

print(P)
MajorStandard = np.array(([a,0]))
MinorStandard = np.array(([0,b]))

xActualEllipse = P@xStandardEllipse
MajorActual = P@MajorStandard
MinorActual = P@MinorStandard

plt.plot(xStandardEllipse[0,:],xStandardEllipse[1,:],label='Standard ellipse')

plt.plot(c[0]+xActualEllipse[0,:],c[1]+xActualEllipse[1,:],label='Actual ellipse')

plt.scatter(0,0)
plt.scatter(c[0],c[1])

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
