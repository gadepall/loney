import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# x1 = symbols('x₁')
y1 = symbols('y')

def line_gen(A,B):
  len =100
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

A =np.array([10,y1])
B =np.array([2,-3])
C = 10
# Equation is ||A-B||=C
D = A-B

# S= list(solveset(Eq((A-B).dot(A-B),C**2),x1))
print((D))
P=np.dot(np.transpose(D),D) - C**2
print((P))
print(type(P))

S= list(solveset(Eq(np.dot(np.transpose(D),D),C**2),y1))

print("The x₁ values are: ",S)

#converting to float
for j in range(len(S)):
  S[j]=round(float(S[j]),2)

print("The x₁ values in float are: ",S)

labels = ['Solution1','Soultion2']
j=0
for i in S:
  P1,P2 = np.array([10,i]),np.array([2,-3])
  x_FP = line_gen(P1,P2)
  plt.plot(x_FP[0,:],x_FP[1,:],label= labels[j])
  j = j + 1
  plt.plot(P1[0], P1[1], 'o')
  plt.text(P1[0] * (1 - 0.1), P1[1] * (1 - 0.5), '({}, {})'.format(P1[0], P1[1]))
  plt.plot(P2[0], P2[1], 'o')
  plt.text(P2[0] * (1 - 0.2), P2[1] * (1 + 0.2), '({}, {})'.format(P2[0], P2[1]))

plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='lower left')
plt.axis('equal')
plt.show()

y = np.linspace(-15,5,1000)
x = []
for p in range(len(y)):
  x1 = P.subs(y1,y[p])
  x.append(x1)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.grid()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='lower left')
j = 0
for i in S:
  P1 = np.array([0,i])
  j = j + 1
  plt.plot(0, P1[1], 'o')
  plt.text(P1[0] * (1 - 0.1), P1[1] * (1 - 0.5), '({}, {})'.format(0, P1[1]))
plt.plot(x,y, 'r',label='y(x)')

# show the plot
plt.show()
