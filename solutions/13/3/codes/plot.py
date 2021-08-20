import numpy as np
import matplotlib.pyplot as plt
from coeffs import * 


M = np.array([-12,1]) #a point satisfying equation1
N = np.array([3,-4])  # another point satisfying equation1
O = np.array([1,5]) #a point satisfying equation2
P = np.array([-3,-7]) #another point satisfying equation2
#Generating all lines
x_AB = line_gen(M,N)
x_CD = line_gen(O,P)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$x+3y+9=0$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$-3x+y-2=0$')
plt.plot(-1.5, -2.5, 'ro', label = 'intersection point(-1.5,-2.5)')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.grid() # minor
plt.axis('equal')
plt.show()
