from fractions import Fraction

# n = int(input('Enter Number Of Data Points : '))
# x_lst, y_lst, del1x, del2x, del3x = [0] * n, [0] * n, [], [], []
# for i in range(n):
#     x_lst[i], y_lst[i] = map(int, input(f'Enter x[{i}] and y[{i}] : ').split())

# x_lst, y_lst = [5, 6, 9, 11], [12, 13, 14, 16]
# x_lst, y_lst = [0, 1, 3, 4], [-12, 0, 12, 24]
x_lst, y_lst = [0, 1, 3, 6], [2, 3, 8, 10]
del1x, del2x, del3x = [], [], []

for i in range(1, len(y_lst)):
    a, b = y_lst[i] - y_lst[i - 1], x_lst[i] - x_lst[i - 1]
    del1x.append(Fraction(a, b))
print(del1x)

for i in range(1, len(del1x)):
    a, b = del1x[i] - del1x[i - 1], x_lst[i + 1] - x_lst[i - 1]
    del2x.append(Fraction(a, b))
print(del2x)

for i in range(1, len(del2x)):
    a, b = del2x[i] - del2x[i - 1], x_lst[i + 2] - x_lst[i - 1]
    del3x.append(Fraction(a, b))
print(del3x)

xp = eval(input('Enter interpolation Point : '))
ans_lst = [0] * 4
ans_lst[0] = y_lst[0]
ans_lst[1] = (xp - x_lst[0]) * del1x[0]
ans_lst[2] = (xp - x_lst[0]) * (xp - x_lst[1]) * del2x[0]
ans_lst[3] = (xp - x_lst[0]) * (xp - x_lst[1]) * (xp - x_lst[2]) * del3x[0]
print(ans_lst)
print('Function value at ', xp, 'is', sum(ans_lst), '=', float(sum(ans_lst)))

# for decimal results

# x_lst, y_lst = [5, 6, 9, 11], [12, 13, 14, 16]
# x_lst, y_lst = [0, 1, 3, 4], [-12, 0, 12, 24]
x_lst, y_lst = [0, 1, 3, 6], [2, 3, 8, 10]
del1x, del2x, del3x = [], [], []

for i in range(1, len(y_lst)):
    a, b = y_lst[i] - y_lst[i - 1], x_lst[i] - x_lst[i - 1]
    del1x.append(round(a / b, 4))
print(del1x)

for i in range(1, len(del1x)):
    a, b = del1x[i] - del1x[i - 1], x_lst[i + 1] - x_lst[i - 1]
    del2x.append(round(a / b, 4))
print(del2x)

for i in range(1, len(del2x)):
    a, b = del2x[i] - del2x[i - 1], x_lst[i + 2] - x_lst[i - 1]
    del3x.append(round(a / b, 4))
print(del3x)

xp = eval(input('Enter interpolation Point : '))
ans_lst = [0.0] * 4
ans_lst[0] = y_lst[0]
ans_lst[1] = (xp - x_lst[0]) * del1x[0]
ans_lst[2] = (xp - x_lst[0]) * (xp - x_lst[1]) * del2x[0]
ans_lst[3] = (xp - x_lst[0]) * (xp - x_lst[1]) * (xp - x_lst[2]) * del3x[0]
print(ans_lst)
print('Function value at ', xp, 'is', round(sum(ans_lst), 4))
