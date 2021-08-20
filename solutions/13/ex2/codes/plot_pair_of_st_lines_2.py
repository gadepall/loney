import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,1)

y1 = ( -5*x - 10 ) / 8
y2 = ( -4*x - 20/3) / 5

plt.plot(x,y1,label=r'$5x+8y+10 = 0$')
plt.plot(x,y2,label=r'$4x+5y+\frac{20}{3} = 0$')

plt.grid(True)
plt.legend()

plt.show()