from sympy import Matrix, symbols, Rational, solve

h = symbols('h')

M = Matrix([[6, h, 11], [h, 12, Rational(31,2)],[11, Rational(31,2), 20]])
eq = M.det()

sol = solve(eq, dict=True)

print(sol)
