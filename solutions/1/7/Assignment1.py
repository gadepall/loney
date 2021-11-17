import numpy as np
import matplotlib.pyplot as plt
from sympy import *

a, m1, m2 = symbols('a m₁ m₂')

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

A = np.array([a*m1**2,2*a*m1])
B = np.array([a*m2**2,2*a*m2])

D = A-B
DT=np.transpose(D)

print("distance between (am₁², 2am₁) and (am₂², 2am₂) is ",simplify(sqrt(np.dot(DT,D))))
