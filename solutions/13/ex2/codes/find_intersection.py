import numpy as np

A = np.array([[6, 17/2], [17/2, 12]])
b = np.array([-11, -31/2])

x = np.linalg.solve(A, b)

print(x)