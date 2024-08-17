# eq1 = list(map(int, input('Enter Equation 1 : ').split()))
# eq2 = list(map(int, input('Enter Equation 2 : ').split()))
# eq3 = list(map(int, input('Enter Equation 3 : ').split()))

# eq1 = [83, 11, -4, 95]
# eq2 = [7, 52, 13, 104]
# eq3 = [3, 8, 29, 71]

eq1 = [3, -1, -1, 2]
eq2 = [-2, 1, -3, -9]
eq3 = [1, 1, 2, 4]

# x_prev, y_prev, z_prev = map(int, input('Enter Initial values : ').split())
x_prev, y_prev, z_prev = 0, 0, 0

for i in range(8):
    x_now = round((1 / eq1[0]) * (eq1[3] - ((eq1[1] * y_prev) + (eq1[2] * z_prev))), 5)
    x_prev = x_now
    y_now = round((1 / eq2[1]) * (eq2[3] - ((eq2[0] * x_prev) + (eq2[2] * z_prev))), 5)
    y_prev = y_now
    z_now = round((1 / eq3[2]) * (eq3[3] - ((eq3[0] * x_prev) + (eq3[1] * y_prev))), 5)
    z_prev = z_now
    print(i+1, '- iteration :', 'x =', x_now, 'y =', y_now, 'z =', z_now)
