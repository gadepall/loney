import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

len = 200
x = np.linspace(-2,2,len)

# Input parameters of given Hyperbola
V1 = np.array(([2, 3/2], [3/2, -2]))
u1 = np.array(([-7/2, 1/2]))
f1 = -2

# Getting the eigenvalues and eigenvectors 
eigenval1, P1 = LA.eig(V1)
# Creating diagonal matrix of eigenvalues
D1 = np.diag(eigenval1)
# Generating the Hyperbola
y1 = np.sqrt((1-eigenval1[1]*(x**2))/eigenval1[0])

# Center of the hyperbola
V_inv1 = LA.inv(V1)
c1 = -V_inv1@u1

# Axes:
k1 = np.sqrt(np.abs(f1 +u1@c1 ))

# Reflection matrix:
R = np.array(([0,1],[1,0]))

# Affine transform 
z1 = np.hstack((np.vstack((x,y1)),np.vstack((x,-y1))))
y_vec1 = k1*P1.T@R@z1+c1[:,None]

# Input parameters of standard hyperrbola:
V2 = np.array(([2.5, 0], [0, -2.5])) # Eigenvalues of V1
u2 = np.array(([0, 0]))
f2 = -5

# Getting the eigenvalues and eigenvectors 
eigenval2, P2 = LA.eig(V2)
# Creating diagonal matrix of eigenvalues
D2 = np.diag(eigenval2)
# Generating the Hyperbola
y2 = np.sqrt((1-eigenval2[1]*(x**2))/eigenval2[0])

# Center of the hyperbola
V_inv2 = LA.inv(V2)
c2 = -V_inv2@u2

# Axes:
k2 = np.sqrt(np.abs(f2 +u2@c2 ))

# Affine transform 
z2 = np.hstack((np.vstack((x,y2)),np.vstack((x,-y2))))
y_vec2 = k2*P2.T@R@z2+c2[:,None]

# Marking the centers:
std_center = [0, 0]
given_center = [1, 1]

# Plotting the given hyperbola
plt.plot(y_vec1[0,0:len],y_vec1[1,0:len], color='b')
plt.plot(y_vec1[0,len:2*len],y_vec1[1,len:2*len], color='b', label = 'Given Hyperbola')


# Plotting standard hyperbola
plt.plot(y_vec2[0,0:len],y_vec2[1,0:len], color ='orange')
plt.plot(y_vec2[0,len:2*len],y_vec2[1,len:2*len], color='orange', label = 'Standard hyperbola')

# Annotating the points:
plt.scatter(std_center[0], std_center[1], color = 'orange', label = 'Center of standard conic')
plt.scatter(given_center[0], given_center[1], color ='b', label = 'Center of given conic')
labels = ['(0, 0)', '(1, 1)']
points = np.vstack((std_center, given_center)).T
for i, txt in enumerate(labels):
    plt.annotate(txt, # this is the text
                 (points[0,i], points[1,i]), 
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center') 

#plt.axhline(1, color='black')
#plt.axvline(1, color='black')
#plt.axhline(0, color='black')
#plt.axvline(0, color='black')

# Labelling the axes
plt.xlabel('$x-axis$');plt.ylabel('$y-axis$')
plt.legend(bbox_to_anchor=(0.8, 1), loc='lower center')
plt.grid()
plt.savefig('hyperbola.png', bbox_inches='tight')
plt.show()
