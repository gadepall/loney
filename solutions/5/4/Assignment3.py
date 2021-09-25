
import numpy as np
import matplotlib.pyplot as plt

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Inputs
n = np.array([-3,5])
c = -15
e1 = np.array([1,0])
e2 = np.array([0,1])
A = c*e1/(n@e1)
B = c*e2/(n@e2)
#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='(-3 5)x=-15')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.001), A[1] * (1) , '$(5,0)$')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1+ 0.01), B[1] * (1) , '$(0,-3)$')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
