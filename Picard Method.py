import sympy as sp
from sympy.abc import x

y0 = y_now = eval(input('Enter y(0) : '))


def Apply_Limits(expr):
    return expr - expr.subs(x, 0)


for i in range(4):
    # function = x + y_now**2
    # function = sp.exp(x) - y_now
    # function = 1 + (x * y_now)
    # function = x + y_now
    function = -1 * x * y_now
    print(y_now := (y0 + Apply_Limits(sp.integrate(function, x))))
