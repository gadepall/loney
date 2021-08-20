#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the libraries 
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import norm
import math
V=np.array([[12,3.5],[3.5,-10]])
u=np.array([[6.5],[22.5]])
f=-35
delta=np.block([[V,u],[u.T,f]])
print("V\n",V)
print("\nu\n",u)
print("\nf",f)
print("\nMatrix delta\n",delta)
print("\nDeterminant of delta")
round(np.linalg.det(delta),10)


# In[2]:


p = np.poly1d([-10, 7, 12]) # form of cm^2+sbm+a=0
print(np.poly1d(p))


# In[3]:


print("roots",p.roots)
# n_i=(-m_i\\1)
k1=5 
k2=-2
# change (k1,k2) to (-5,2),(2,-5),(10,-1),(-10,1) and verify the results
n1=np.array([0.8*k1,k1]) #straight line 1 equation 
n2=np.array([-1.5*k2,k2]) #straight line 2 equation 
np.convolve(n1,n2)


# In[4]:


num=np.dot(n1,n2) 
norm1=norm(n1) #norm of normal vector n1
norm2=norm(n2) #norm of normal vector n2
val=num/(norm1*norm2)
angle=round(math.degrees(math.acos(val))) #angle between two straight lines
print("Angle between the two straight lines in degrees : \n"+str(angle)+" degrees")


# In[5]:


y_1 = 1.5*x+3.5 # straight line 1
y_2 = -0.8*x+1 # straighe line 2
plt.plot(x, y_1, '-r', label='3X-2y+7=0')
plt.title('Graph of 2y=3x+7')
plt.plot(x, y_2, '-b', label='4X+5y-5=0')
plt.title('Graph of two straight lines')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='best')
plt.grid()
plt.show()


# In[6]:


x = np.linspace(-5,5,100)
y_1 = 1.5*x+3.5 # straight line 1
y_2 = -0.8*x+1 # straighe line 2
plt.plot(x, y_1, '-r', label='3X-2y+7=0')
plt.title('Graph of 2y=3x+7')
plt.plot(x, y_2, '-b', label='4X+5y-5=0')
plt.title('Graph of two straight lines')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='best')
plt.grid()
plt.show()


# In[ ]:




