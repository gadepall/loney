from sympy import Matrix, Rational

M1 = Matrix([[-1, -0.5], [-0.5, 6]])

P, D = M1.diagonalize()

print(P)
print(D)
#print(P.transpose)
