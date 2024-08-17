# import math as m


def Secant(func, a, b):
    for i in range(5):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        c = round(c, 6)
        print(f'Iteration {i + 1} -> {c}')
        a, b = b, c


fun = lambda x: x ** 3 - 5 * x + 1  # interval(0,1)
# fun = lambda x: m.cos(x) - x*m.exp(x)
# fun = lambda x: x * m.log10(x) - 1.2
# fun = lambda x: 2 * x - 6 - m.log10(x)


vals = map(eval, input('Enter Interval ? ').split())
Secant(fun, *vals)
