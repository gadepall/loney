import numpy as np
from matplotlib import pyplot as plt
from math import pi

C = np.array([0 , 0])    #Center Point
F = np.array([0, 0.75, -0.75])  #Foci Point
D = np.array([0 , 4.02 , -4.02]) #Directrix Point
a=2    #semi minor axis
b=3    #semi major axis

t = np.linspace(0, 2*pi, 100)
plt.plot( C[0]+a*np.sin(t) , C[1]+b*np.cos(t), color= 'b', label='Ellipse')
plt.scatter(C[0], C[1] , color= 'b', marker = 'o',label='Center')
plt.axhline(y=4.02, color= 'r')
plt.axhline(y=-4.02, color= 'r')
plt.plot(D[0] , D[1] , 'r', label='Directrix')
plt.plot(D[0] , D[2] , 'r', )
plt.plot(F[0] , F[1] , 'go', label='Foci')
plt.plot(F[0] , F[2] , 'go' )

plt.text(C[0] * (1 - 0.1), C[1] * (1 - 0.2) , '(0,0)')
plt.text(D[0], D[1] , 'y= 9/√5')
plt.text(D[0], D[2] , 'y= -9/√5')
plt.text(F[0] * (1 - 0.1), F[1] * (1 - 0.2) , '(0, √5/3)')
plt.text(F[0] * (1 - 0.1), F[2] * (1 - 0.2) , '(0, -√5/3)')

plt.title("Plot of Ellipse")
plt.xlabel("X- Axis")
plt.ylabel("Y- Axis")
plt.grid(True)
plt.legend(loc='best')
plt.show()

