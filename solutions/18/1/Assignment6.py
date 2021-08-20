# Plot of the equation of the tangent to a circle x^2+y^2−3x+10y=15 passing through the point (4,-11).
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

p= np.array([4,-11])
u = np.array([-3/2,5])
f = -15
c=-u
r = np.sqrt(LA.norm(c)**2-f)
x_circ= circ_gen(c,r)
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')

x=np.arange(-1,10)
co=np.transpose(u)@p + f	# constant c of tangent equation(n^T*x=c)
fo=u + p			# Normal Vector n of the tangent equation.
y=(1/fo[1])*(-co-fo[0]*x)
plt.plot(x,y,label='$tangent$')

plt.annotate("(4, -11)", (4, -11), (4.5, -11.5))
plt.annotate("(1.5, -5)", (c[0], c[1]), (c[0]+0.2, c[1]))

plt.scatter(4,-11,color='blue')
plt.scatter(c[0],c[1],color='red')

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()
