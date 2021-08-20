import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(10,40,100)
y_1 = 3*x-13 
y_2 = 2*x+10.5 
plt.figure(1)
plt.plot(x, y_1, '-r', label='-3x+y=-13')
plt.plot(x, y_2, '-b', label='-4x+2y=21')
plt.title('Graph of two straight lines')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid()
plt.savefig('Figure1.png')


x = np.linspace(-5,5,100)
y_3 = 8*x-(102/59)
y_4 = (3/4)*x+(59/58)
plt.figure(2)
plt.plot(x, y_3, '-r', label='-232x+29y=-102')
plt.plot(x, y_4, '-b', label='-87x+116y=118')
plt.title('Graph of two straight lines')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid()
plt.savefig('Figure2.png')
