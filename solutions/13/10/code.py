import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,10,500)
y_1 = 0*x+3/2
y_2 = 0*x+4/3
plt.figure(1)
plt.plot(x,x*0+1.5)
plt.plot(x*0+4/3,x)
plt.grid(linestyle='dotted')
plt.xlim(-2,8)
plt.ylim(-2,8)

plt.title('Graph of pair of straight lines', fontsize=8)
plt.figure(2)
plt.plot(x,(12+8*x)/9)
plt.grid(linestyle='dotted')

plt.show()
#plt.savefig("two_straight_lines_intersection_point_01.png", bbox_inches='tight')
