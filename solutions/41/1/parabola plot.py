import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

def parab_gen(y,a):
    x = y**2/a
    return x

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-5,5,len)


#parab parameters
V = np.array(([1,-4],[-4,16]))
u = np.array(([0,-51/2]))
f = 0

O = np.array(([0,0]))
#Generating the Standard parabola

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)

D = np.diag(D_vec)
p = P[:,1]
eta = (u@p)
foc = np.abs(2*u@p)/D_vec[1]

x = parab_gen(y,foc)
cA = np.vstack((u+eta*p,V))
cb = np.vstack((-f,(eta*p-u).reshape(-1,1)))
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()

c1 = np.array(([(u@V@u-2*D_vec[0]*u@u+D_vec[0]**2*f)/(eta*D_vec[1]**2),0]))
xStandardparab = np.vstack((x,y))

xActualparab = P@xStandardparab + c[:,np.newaxis]

parab_coords = np.vstack((O,c)).T
plt.scatter(parab_coords[0,:], parab_coords[1,:])
vert_labels = ['$O$','$c$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (parab_coords[0,i], parab_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.plot(xActualparab[0,:],xActualparab[1,:],label='Parabola', color='r')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
