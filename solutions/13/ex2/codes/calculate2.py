import math
from sympy import Rational

lambda1 = 9 - 3*Rational(math.sqrt(3649),20)
lambda2 = 9 + 3*Rational(math.sqrt(3649),20)

u1 = Rational(-math.sqrt(3649)-20,57)
u2 = 1
v1 = Rational(-20 + math.sqrt(3649),57)
v2 = 1

norm1 = math.sqrt(u1**2 + u2**2)
norm2 = math.sqrt(v1**2 + v2**2)

u1 = Rational(u1, norm1)
u2 = Rational(u2, norm1)
v1 = Rational(v1, norm2)
v2 = Rational(v2, norm2)

alpha = 1
beta = -2

q = math.sqrt(-Rational(lambda2,lambda1))

a1 = u1 + q*v1
b1 = u2 + q*v2
c1 = - alpha*u1 - beta*u2 - q*alpha*v1 - q*beta*v2  

print(a1)
print(b1)
print(c1)

a2 = u1 - q*v1
b2 = u2 - q*v2
c2 = - alpha*u1 - beta*u2 + q*alpha*v1 + q*beta*v2

print(a2)
print(b2)
print(c2)