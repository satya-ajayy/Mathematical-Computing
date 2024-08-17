import sympy as sp
from sympy.abc import a, t, s


class LaplaceTransforms:
    @staticmethod
    def L(func):
        return sp.laplace_transform(func, t, s, noconds=True)

    @staticmethod
    def invL(func):
        return sp.inverse_laplace_transform(func, s, t, noconds=True)


if __name__ == '__main__':
    solver = LaplaceTransforms()
    exp, sin, cos = sp.exp, sp.sin, sp.cos
    lst1 = [1, t, exp(-a * t), t * exp(-a * t), sin(a * t),
            cos(a * t), (cos(4 * t) * sin(2 * t)) / t]
    lst2 = [1/s**2]
    for i in lst1:
        ans = solver.invL(i)
        print(ans)
