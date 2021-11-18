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



A =np.array([1,-3])
B =np.array([-2,1])

D=np.linalg.norm(A-B)


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
