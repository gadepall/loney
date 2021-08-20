import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linalg as LA

def ellipse_gen(a,b,center):
    len = 50
    theta = np.linspace(0,2*np.pi,len)
    x_ellipse = np.zeros((2,len))
    x_ellipse[0,:] = a*np.cos(theta) + center[0]   #acos(t)+h
    x_ellipse[1,:] = b*np.sin(theta) + center[1]   #asin(t)+k
    return x_ellipse
 
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-5,5,len)
 
#Ellipse parameters
V = np.array(([13,-9],[-9,37]))
u = np.array(([1,7]))
f = -2

#Computation
utV_1u = np.matmul(np.matmul(u.T,np.linalg.inv(V)),u)
c = -np.linalg.inv(V)@u

#Eigenvalues and eigenvectors
D_vec,P = np.linalg.eig(V)
D = np.diag(D_vec)
a = np.sqrt((utV_1u-f)/D_vec[0])
b = np.sqrt((utV_1u-f)/D_vec[1])
xStandardEllipse = ellipse_gen(a,b,[0,0])

#Major and Minor Axes
MajorStandard = np.array(([a,0]))
MinorStandard = np.array(([0,b]))
 
#Affine transform 
Cs = np.array([[c[0],c[1]] for i in range(50)]).T
xActualEllipse = P@xStandardEllipse + Cs # x = Py + c (Affine Transformation)
MajorActual = P@MajorStandard+c[0]
MinorActual = P@MinorStandard+c[1]
 
#Plotting the standard ellipse
plt.plot(xStandardEllipse[0,:],xStandardEllipse[1,:],label='Standard Ellipse')
 
#Plotting the actual ellipse
plt.plot(xActualEllipse[0,:],xActualEllipse[1,:],label='Actual Ellipse')
 
#Labeling the coordinates
tri_coords = np.vstack((MajorStandard,MinorStandard,MajorActual,MinorActual,c)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['$a$','$b$','$a^{\prime}$','$b^{\prime}$','$\mathbf{c}$']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# Axis Plots
x_ = np.linspace(-0.9,0.9,50)
y_ = np.linspace(-0.6,0.6,50)
y_1 = [0 for i in range(50)]          
x_1 = [0 for i in range(50)]          
plt.plot(x_, y_1, 'black')
plt.plot(x_1,y_, 'black')

plt.xlabel('$X Axis$')
plt.ylabel('$Y Axis$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
 
plt.show()
