import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,1)

y1 = ( -2*x - 4 ) / 3
y2 = ( -3*x - 5) / 4

plt.plot(x,y1,label='$2x+3y+4 = 0$')
plt.plot(x,y2,label='$3x+4y+5 = 0$')

plt.grid(True)
plt.legend()

plt.show()

