n = int(input('Enter Number Of Data Points : '))
x_lst, y_lst, ans_lst = [0]*n, [0]*n, []

for i in range(n):
    x_lst[i], y_lst[i] = map(float, input(f'Enter x[{i}] & y[{i}] : ').split())

xp = eval(input('Enter interpolation Point : '))
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p *= (xp - x_lst[j])/(x_lst[i] - x_lst[j])
    ans_lst.append(p * y_lst[i])

print(ans_lst)
print('value at ', xp, 'is', sum(ans_lst))
