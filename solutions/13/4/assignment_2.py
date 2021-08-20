import numpy as np
import matplotlib.pyplot as plt

#Plotting all lines
x = np.linspace(-10, 10, 80)
y1=(1-x)/2
y2 =5+4*x
plt.plot(x,y1, label ='x+2y-1=0')
plt.plot(x,y2, label = '-4x+y-5=0')
plt.plot(-1, 1, "ro", label ='intersection point(-1,1)')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
#plt.savefig('hw2plot.png')
plt.show()
