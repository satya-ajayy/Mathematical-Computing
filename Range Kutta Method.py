# def f(x, y): return x + y ** 2
def f(x, y): return (y**2 - x**2)/(y**2 + x**2)
# def f(x, y): return x + x**2 + y
# def f(x, y): return x + y


def Range_Kutta(x_start, y_start, x_last, h):
    while x_start < x_last:
        k1 = round(h * (f(x_start, y_start)), 6)
        k2 = round(h * (f((x_start + h / 2), (y_start + k1 / 2))), 6)
        k3 = round(h * (f((x_start + h / 2), (y_start + k2 / 2))), 6)
        k4 = round(h * (f((x_start + h), (y_start + k3))), 6)
        k = round(((k1 + 2 * k2 + 2 * k3 + k4) / 6), 6)
        y_last = round(y_start + k, 6)
        print(f'Iteration With x = {x_start} and y = {y_start}')
        print(f'k1 = {k1}  k2 = {k2}  k3 = {k3} k4 = {k4} ')
        print(f'k = {k}  y({x_start+h}) = {y_last}\n')
        y_start, x_start = y_last, x_start + h


x0, y0 = map(eval, input('Enter x0 and y0 : ').split())
xn = eval(input('Enter Final point : '))
height = eval(input('Enter height : '))
Range_Kutta(x0, y0, xn, height)
