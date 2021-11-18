import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

a=2
b=3
A =np.array([a,0])
B =np.array([0,b])

# method 1
D=np.linalg.norm(A-B)

# method 2
D=np.sqrt((A-B).dot((A-B)))

print("The distance between ",A," and ",B," is: ",D)

#Generating all lines
x_AB = line_gen(A,B)

#Plotting Line between A and B
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.3), B[1] * (1-0.1) , 'B')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
