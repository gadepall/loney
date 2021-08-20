from sympy import Matrix, Rational

M1 = Matrix([[6, 8.5], [8.5, 12]])

P, D = M1.diagonalize()

print(P)
print(D)
#print(P.transpose)