import math as m
import tabulate as tb


def Regula_Falsi(func, a, b):
    helper = list()
    header = ['Iteration', 'Root', 'Func_value']
    for i in range(8):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        helper.append([i+1, round(c, 6), round(func(c), 6)])
        a = round(c, 6)
    print(tb.tabulate(helper, headers=header, tablefmt='pretty'))


# fun = lambda x: x ** 3 - 2 * x - 5
# fun = lambda x: m.cos(x) - x*m.exp(x)
# fun = lambda x: x * m.log10(x) - 1.2
# fun = lambda x: 2 * x - 6 - m.log10(x)
fun = lambda x: 3 * x - m.sqrt(1 + m.sin(x))

vals = map(eval, input('Enter Interval ? ').split())
Regula_Falsi(fun, *vals)
