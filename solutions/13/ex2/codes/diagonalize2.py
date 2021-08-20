from sympy import Matrix, Rational

M1 = Matrix([[6, Rational(171,20)], [Rational(171,20), 12]])

P, D = M1.diagonalize()

print(P)
print(D)
#print(P.transpose)