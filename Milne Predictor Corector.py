def milne(xp4, h, y_lst, f_lst, func):

    print(f_lst)
    yp4 = y_lst[0] + 4 * h * ((2 * (f_lst[3] + f_lst[1]) - f_lst[2]) / 3)
    print('milne predictor value at', xp4, 'is %.6f' % yp4)
    yc4 = y_lst[2] + (h / 3) * (f_lst[2] + func(xp4, yp4) + (4 * f_lst[3]))
    print('milne corrector value at', xp4, 'is %.6f' % yc4)
    print(f'f({xp4}) = ', func(xp4, yc4))
    return yc4


def main():
    fun = lambda x, y: round(x - y**2, 6)
    x_list = [0, 0.2, 0.4, 0.6]
    y_list = [0, 0.02, 0.0795, 0.1762]
    h = x_list[1] - x_list[0]
    f_list = [fun(x, y) for x, y in zip(x_list, y_list)]
    xp4 = eval(input('Enter Final x : '))
    yc4 = milne(xp4, h, y_list, f_list, fun)

    if input('Need Next Iteration : '):
        x_list.append(x_list[-1] + h)
        y_list.append(yc4)
        f_list = [fun(x, y) for x, y in zip(x_list[1:], y_list[1:])]
        milne((xp4+h), h, y_list[1:], f_list, fun)


if __name__ == '__main__':
    main()
