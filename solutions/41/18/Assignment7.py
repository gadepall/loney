#Trace the following central conic :  x^2 + y^2 + xy + x + y = 1
import numpy as np
import matplotlib.pyplot as plt

def ellipse_gen(a,b) :
  y_el=np.zeros((2,50))
  rad=np.linspace(0,2*np.pi,50)
  y_el[0,]=a*np.cos(rad)
  y_el[1,]=b*np.sin(rad)
  return y_el

V=np.array([1,0.5,0.5,1]).reshape(2,2)
u=np.array([0.5,0.5])
f=-1
lam,P = np.linalg.eig(V)
D=np.diag(lam)
V_inv=np.linalg.inv(V)
c=-V_inv@u
a=np.sqrt((np.transpose(u)@V_inv@u - f)/lam[0])
b=np.sqrt((np.transpose(u)@V_inv@u - f)/lam[1])
y_el=ellipse_gen(a,b)

print("a (minor axis) : {}".format(a))
print("b (major axis) : {}".format(a))
print("center         : {}".format(a))

x_el=np.empty((1,2))
for i in y_el.T:
  x_el=np.vstack((x_el,P@i.T +c))
x_el=x_el.T

plt.plot(y_el[0,],y_el[1,],label='Standard Ellipse')
plt.plot(x_el[0,],x_el[1,],label='Actual Ellipse')
plt.annotate("(-0.3,-0.3)", (c[0], c[1]), (c[0]-0.4, c[1]-0.25))
plt.scatter(c[0],c[1],color='red')
plt.scatter(0,0,color='black')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()
