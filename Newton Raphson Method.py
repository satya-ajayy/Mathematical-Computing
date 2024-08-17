import math as m


def Newton_Raphson(func, drv_func, x_now):
    for i in range(5):
        x_now = round(x_now - (func(x_now)/drv_func(x_now)), 6)
        print(f'x{i+1} = {x_now}', end='  ')


# fun = lambda x: x ** 3 - 3 * x - 5
# drv_fun = lambda x: 3*x ** 2 - 3

# fun = lambda x: m.cos(x) - x*m.exp(x)
# drv_fun = lambda x: -1*m.sin(x) - m.exp(x)*(x+1)

fun = lambda x: 2*x - 6 - m.log10(x)
drv_fun = lambda x: 2 - (0.4343 / x)

x0 = eval(input('Enter start point ? '))
Newton_Raphson(fun, drv_fun, x0)
