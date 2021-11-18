import numpy as np
import matplotlib.pyplot as plt

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

m=2
n=3

A =np.array([-1,2])
B =np.array([4,-5])

P=((m*B)+(n*A))/(m+n)

Q=((m*B)-(n*A))/(m-n)


x_AB = line_gen(A,B)



plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')


plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.001), A[1] * (1 - 0.001) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.1), B[1] * (1-0.1) , 'B')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1-0.1), P[1] * (1-0.3) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1+0.1), Q[1] * (1-0.001) , 'Q')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
