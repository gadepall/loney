import numpy as np
import matplotlib.pyplot as plt
from coeffs import * 


M = np.array([-8,-7]) #a point satisfying equation1
N = np.array([8,1])  # another point satisfying equation1
O = np.array([9,-5]) #a point satisfying equation2
P = np.array([-9,1]) #another point satisfying equation2
#Generating all lines
x_AB = line_gen(M,N)
x_CD = line_gen(O,P)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$-x+2y+6=0$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$x+3y+6=0$')
plt.plot(1.2, -2.4, 'ro', label = 'intersection point(6/5,-12/5)')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.grid() # minor
plt.axis('equal')
plt.show()
