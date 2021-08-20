#Program to plot  the asymptotes of a hyperbola
#Code by GVV Sharma
#Released under GNU GPL
#October 3, 2020

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA


#Generating points on a parabola
def parab_gen(y,a):
	x = y**2/a
	return x
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 
def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB


#Intersection of two lines
def line_intersect(n1,A1,n2,A2):
  N=np.vstack((n1,n2))
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.inv(N)@p
  return P

#Intersection of two lines
def perp_foot(n,cn,P):
  m = omat@n
  N=np.block([[n],[m]])
  p = np.zeros(2)
  p[0] = cn
  p[1] = m@P
  #Intersection
  x_0=np.linalg.inv(N)@p
  return x_0
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-2,2,len)

#parab parameters
V = np.array(([4,-2],[-2,1]))
u = np.array(([-6,3]))
f = 9
#p = np.array(([1,0]))
#foc = np.abs(p@u)/2

O = np.array(([0,0]))
#Generating the Standard parabola

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
#print(P)
p = P[:,0]
eta = 2*u@p
#foc = np.abs(eta/D_vec[1])
foc = eta/D_vec[1]
#print(p,foc,D_vec[1])
x = parab_gen(y,foc)
#Affine Parameters
#c1 = np.array(([-(u@V@u-2*u@u+f)/(2*u@p),0]))
#c = -P@u+c1
#print(c1)
#p = -p
cA = np.vstack((u+eta*0.5*p,V))
cb = np.vstack((-f,(eta*0.5*p-u).reshape(-1,1)))
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()
print(c,-29/25,22/25,foc)
#print(c,foc)
#print(cA,cb)
#print(p,c)  
P=-P
c1 = np.array(([(u@V@u-2*D_vec[0]*u@u+D_vec[0]**2*f)/(eta*D_vec[0]**2),0]))
xStandardparab = np.vstack((x,y))
#xActualparab = P@(xStandardparab - c1[:,np.newaxis])-u[:,np.newaxis]/D_vec[1]
xActualparab = P@xStandardparab + c[:,np.newaxis]
#xActualparab = P@xStandardparab 

##Tangent Analysis
#m_0 = 2/3
#m = np.array(([1,m_0]))
#n = omat@m
#kappa = p@u/(p@n)
#
#qA = np.vstack((u+kappa*n,V))
#qb = np.vstack((-f,(kappa*n-u).reshape(-1,1)))
#q = LA.lstsq(qA,qb,rcond=None)[0]
#q = q.flatten()
#O = np.array([0,0])
#print(c,q)
#
##Generating the tangent
#k1 = 2
#k2 = -2
#x_AB = line_dir_pt(m,q,k1,k2)
#
#Labeling the coordinates
#parab_coords = np.vstack((O,c)).T
#plt.scatter(parab_coords[0,:], parab_coords[1,:])
#vert_labels = ['$O$','$c (-1.16,0.88)$']
#for i, txt in enumerate(vert_labels):
#    plt.annotate(txt, # this is the text
#                (parab_coords[0,i], parab_coords[1,i]), # this is the point to label
#               textcoords="offset points", # how to position the text
#                 xytext=(0,5), # distance from text to points (x,y)
#                 ha='center') # horizontal alignment can be left, right or center

#Plotting all lines
#plt.plot(x_AB[0,:],x_AB[1,:],label='Tangent')

#Plotting the actual parabola
#plt.plot(xStandardparab[0,:],xStandardparab[1,:],label='Parabola',color='r')
plt.plot(xActualparab[0,:],xActualparab[1,:],label='Pair of coincident lines',color='r')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
