import math as m


def Iteration(func, x_start):
    for i in range(8):
        x_start = round(func(x_start), 6)
        print(f'Iteration {i+1} -> {x_start}')


# fun = lambda x: x ** 3 + x**2 - 1
# taken_fun = lambda x: 1 / m.sqrt(x + 1)

fun = lambda x: m.cos(x) - 3 * x + 1
taken_fun = lambda x: (1 + m.cos(x)) / 3

start = eval(input('Enter x0 : '))
Iteration(taken_fun, start)
