import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,10,500)
y_1 = 3*x+2
y_2 = 2*x+.5
plt.figure(1)
plt.plot(x,y_1,label='(-6 2)x=4')
plt.plot(x,y_2,label='(-2 1)x=.5');
plt.grid(linestyle='dotted')
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.title('Graph of pair of straight lines', fontsize=8)
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()
