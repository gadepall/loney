
import numpy as np
from matplotlib import pyplot as plt
from math import pi

A = np.array([1.8 , 0])
B = np.array([0 , -1.3])

X = ([A[0], B[0]])
Y = ([A[1], B[1]])

plt.plot(X, Y, 'r', label='(5  -7)x=9')

plt.plot(A[0] , A[1] , 'go' )
plt.plot(B[0] , B[1] , 'go' )

plt.text(A[0], A[1] , '(9/5, 0)')
plt.text(B[0], B[1] , '(0, -9/7)')

plt.title("Plot of Straight Line")
plt.xlabel("X- Axis")
plt.ylabel("Y- Axis")
plt.grid(True)
plt.legend(loc='best')
plt.show()
