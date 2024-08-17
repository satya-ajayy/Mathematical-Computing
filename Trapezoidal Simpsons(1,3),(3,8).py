# import mpmath
# import sympy as sp
import math
import numpy as np
from fractions import Fraction


def Trapezodial(x_list, y_list):
    ans = ((y_list[0] + y_list[-1]) / 2) + sum(y_list[1:-1])
    key = float(ans * (x_list[1] - x_list[0]))
    print('Trapezodial Answer : ', round(key, 10))


def Simpsons13(x_list, y_list):
    try:
        assert (len(x_list) % 2) == 0
        ans = (y_list[0] + y_list[-1]) + (4 * sum(y_list[1:-1:2]))
        ans += (2 * sum(y_list[2:-1:2]))
        key = float((ans * (x_list[1] - x_list[0])) / 3)
        print('Simpsons1/3 Answer : ', round(key, 10))
    except AssertionError:
        print('Simpsons1/3 rule is only applicable to multiples of 2')


def Simpsons38(x_list, y_list):
    try:
        assert (len(x_list) % 3) == 0
        ans = (y_list[0] + y_list[-1]) + (2 * sum(y_list[3:-1:3]))
        ans += (3 * sum([y_list[i] for i in range(1, len(y_list) - 1) if i % 3 != 0]))
        key = float((ans * 3 * (x_list[1] - x_list[0])) / 8)
        print('Simpsons3/8 Answer : ', round(key, 10))
    except AssertionError:
        print('Simpsons3/8 rule is only applicable to multiples of 3')


def main():
    a, b = map(float, input('Enter Limits a & b: ').split())
    n = int(input('Enter n : '))
    x_list = [Fraction(i).limit_denominator(n) for i in np.linspace(a, b, n)]
    # y_list = [sp.exp(i) for i in x_list]
    # y_list = [1 / (1 + i ** 2) for i in x_list]
    # y_list = [mpmath.ln(i) for i in x_list]
    y_list = [i / math.sqrt(1+i**5) for i in x_list]
    print(x_list, '\n', y_list), Trapezodial(x_list, y_list)
    Simpsons13(x_list, y_list), Simpsons38(x_list, y_list)


if __name__ == '__main__':
    main()
