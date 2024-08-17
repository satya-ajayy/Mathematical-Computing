# eq1 = list(map(int, input('Enter Equation 1 : ').split()))
# eq2 = list(map(int, input('Enter Equation 2 : ').split()))
# eq3 = list(map(int, input('Enter Equation 3 : ').split()))

eq1 = [5, -1, 3, 10]
eq2 = [3, 6, 0, 18]
eq3 = [1, 1, 5, -10]

# x_prev, y_prev, z_prev = map(int, input('Enter Initial values : ').split())
x_prev, y_prev, z_prev = 3, 0, -2

for i in range(20):
    x_now = round((1 / eq1[0]) * (eq1[3] - ((eq1[1] * y_prev) + (eq1[2] * z_prev))), 5)
    y_now = round((1 / eq2[1]) * (eq2[3] - ((eq2[0] * x_prev) + (eq2[2] * z_prev))), 5)
    z_now = round((1 / eq3[2]) * (eq3[3] - ((eq3[0] * x_prev) + (eq3[1] * y_prev))), 5)
    print(i + 1, '- iteration :', 'x =', x_now, 'y =', y_now, 'z =', z_now)
    x_prev, y_prev, z_prev = x_now, y_now, z_now
