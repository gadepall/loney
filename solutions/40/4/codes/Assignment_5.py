import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-2,2,len)

#hyper parameters
V = np.array(([2,-36],[-36,23]))
u = np.array(([-2,-1]))
f = -48
Vinv = LA.inv(V)

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)

uconst = u.T@Vinv@u-f
a = np.sqrt(np.abs(uconst/D_vec[0]))
b = np.sqrt(np.abs(uconst/D_vec[1]))

#Generating the Standard Hyperbola
x = np.sqrt(1+y**2)   #x = hyper_gen(y)   
xStandardHyperLeft = np.vstack((-x,y))
xStandardHyperRight = np.vstack((x,y))

#Affine Parameters
c = -Vinv@u
#print(c[0],c[1])
R =  np.array(([0,1],[1,0]))
ParamMatrix = np.array(([a,0],[0,b]))

#Generating the eigen hyperbola
xeigenHyperLeft = R@ParamMatrix@xStandardHyperLeft
xeigenHyperRight = R@ParamMatrix@xStandardHyperRight

#Generating the actual hyperbola
xActualHyperLeft = P@ParamMatrix@R@xStandardHyperLeft+c[:,np.newaxis]
xActualHyperRight = P@ParamMatrix@R@xStandardHyperRight+c[:,np.newaxis]

#Hyperbola vertices   ## didn't get this
V1old = np.array([1,0])
V2old = -V1old

V1 = P@R@ParamMatrix@V1old+c
V2 = P@R@ParamMatrix@V2old+c

#Plotting the eigen hyperbola
plt.plot(xeigenHyperLeft[0,:],xeigenHyperLeft[1,:],label='Standard hyperbola',color='b')
plt.plot(xeigenHyperRight[0,:],xeigenHyperRight[1,:],color='b')

#Plotting the actual hyperbola
plt.plot(xActualHyperLeft[0,:],xActualHyperLeft[1,:],label='Actual hyperbola',color='r')
plt.plot(xActualHyperRight[0,:],xActualHyperRight[1,:],color='r')


#Labeling the coordinates
# hyper_coords = np.vstack((q1,q2,c)).T
# plt.scatter(hyper_coords[0,:], hyper_coords[1,:])
# vert_labels = ['$q_1$','$q_2$','$c$']
# for i, txt in enumerate(vert_labels):
#     plt.annotate(txt, # this is the text
#                  (hyper_coords[0,i], hyper_coords[1,i]), # this is the point to label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') # horizontal alignment can be left, right or center

##plt.scatter(c)
plt.plot(c[0],c[1],marker='o',color='black') # origin point 
plt.annotate('$c(-41/625,-37/625)$',c,textcoords="offset points",xytext=(0,10),ha='center')

#
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')


plt.show()
