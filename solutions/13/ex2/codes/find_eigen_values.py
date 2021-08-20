from sympy import Matrix, Rational #Symbols

#M1 = Matrix([[6, Rational(17,2)], [Rational(17,2), 12]])
#M2 = Matrix([[6, Rational(171,2)], [Rational(171,2), 12]])

M1 = Matrix([[6, Rational(17,2), 22], [Rational(17,2), 12, 31], [22, 31, 20]])
M2 = Matrix([[6, Rational(171,2), 22], [Rational(171,2), 12, 31], [22, 31, 20]])

eigvals = M1.eigenvals()
eigvects = M1.eigenvects()

P, D = M1.diagonalize(0)
print(eigvals)
print(eigvects)

#x, y = Symbols('x','y')
#X = [[x, y]]

#solve


