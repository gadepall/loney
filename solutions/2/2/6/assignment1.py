import numpy as np
np.__version__
import matplotlib.pyplot as plt


A = np.array([-1,2])

B =np.array([2,3])

C= np.array([4,-3])

BA= B-A
CA = C-A

x = np.array([-1,2,4])
y=np.array([2,3,-3])
x=x+1
y=y-2

coord = ['A','B','C']

plt.quiver([0, 0], [0, 0],[3, 5], [ 1, -5],color=['g','r'], angles='xy', scale_units='xy', scale=1)
plt.xlim(-5, 7)
plt.ylim(-7, 7)

plt.scatter([0,3,5], [0, 1, -5],color='k')

for i in range(3):
  plt.text(x[i],y[i],'{}({},{})'.format(coord[i],x[i],y[i]))


plt.text(1.5,1,'B-A')
plt.text(2.5,-2,'C-A')

plt.title('Vector Representation of triangle')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.grid()
plt.plot([3,5],[1,-5],'b--')
plt.show()



BA_X_CA = np.cross(BA,CA)
Norm=np.linalg.norm(BA_X_CA)

Area = (1/2)*Norm
print('Area of triangle is {:.2f} square units.'.format(Area))