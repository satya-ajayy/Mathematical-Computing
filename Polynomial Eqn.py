import sympy as sp
from sympy.abc import a, b, c, d, x, y

# this is the process to get equation from points,
# or you may calculate equations and give manually as shown in comment lines 18,19
arr1, arr2 = [], []
# points = [(-3, -53), (-2, -18), (2, 2), (3, 7)]
# points = [(5, 12), (6, 13), (9, 14), (11, 16)]
points = [(0, -12), (1, 0), (3, 12), (4, 24)]

for p, q in points:
    expr = a * x ** 3 + b * x ** 2 + c * x + d + y
    # print(str(expr.subs(x, p).subs(y, q).simplify()))
    arr1.append([p ** 3, p ** 2, p, 1])
    arr2.append([q])

# print(arr1, arr2)
# arr1 = [[-27, 9, -3, 1], [-8, 4, -2, 1], [8, 4, 2, 1], [27, 9, 3, 1]]
# arr2 = [[-53], [-18], [2], [7]]

m1, m2 = sp.Matrix(arr1), sp.Matrix(arr2)
L = sp.matrices.MatrixBase.solve(m1, m2)
print(L[0], 'x^3 +', L[1], 'x^2 +', L[2], 'x^1 +', L[3])
exp = L[0] * x ** 3 + L[1] * x ** 2 + L[2] * x + L[3]
