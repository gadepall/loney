# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:10:51 2020

@author: sandh
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
x, y = np.meshgrid(x, y)

def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)
    
axes()
plt.contour(x, y, 19*x*x+24*x*y+1*y*y-22*x-6*y+0, [0], colors='k')
plt.contour(x, y, 19*x*x+24*x*y+1*y*y-22*x-6*y+4, [0], colors='r')
plt.contour(x, y, 19*x*x+24*x*y+1*y*y-22*x-6*y+8, [0], colors='g')
plt.savefig('./hyperbola.jpg')
plt.show()