# import math as m

def Bisection_Method(func, a, b):
    for i in range(15):
        c = round((a + b) / 2, 6)
        fc = round(func(c), 6)
        print(f'Iteration {i + 1}')
        print(f'a = {a} b = {b} c = {c} f({c}) = {fc}')
        if fc > 0:
            b = c
        else:
            a = c


# fun = lambda x: x ** 3 - x - 1  # interval(1,2)
fun = lambda x: x ** 3 - 2 * x - 5  # interval(2, 3)
# fun = lambda x: m.cos(x) - x*m.exp(x)
# fun = lambda x: x * m.log10(x) - 1.2
# fun = lambda x: 2 * x - 6 - m.log10(x)


vals = map(eval, input('Enter Interval ? ').split())
Bisection_Method(fun, *vals)
