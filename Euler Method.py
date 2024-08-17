# import sympy as sp
import tabulate as tb


class Euler:
    def __init__(self, func):
        self.lst, self.func = list(), func

    def Euler_Method(self, x_now, y_now, height, final):
        while x_now < final:
            ans = round(y_now + height * self.func(x_now, y_now), 6)
            self.lst.append([f'y({round(x_now + height, 3)})', ans])
            x_now, y_now = x_now + height, ans
        header = ['S.No', 'Func Value', 'Answer']
        print(tb.tabulate(self.lst, header, tablefmt='pretty', showindex=True))

    def Modified_Euler(self, x_now, y_now, height, final):
        while x_now < final:
            ans = round(y_now + height * self.func(x_now, y_now), 6)
            helper = [f'y({round(x_now + height, 3)})', ans]
            for i in range(5):
                mod_ans = self.func(x_now, y_now) + self.func((x_now + height), ans)
                helper.append(ans := round(y_now + (height / 2) * mod_ans, 6))
            self.lst.append(helper)
            x_now, y_now = x_now + height, ans
        header = ['S.No', 'Func Value', 'Answer', *[f'Mod_Ans{i}' for i in range(1, 5 + 1)]]
        print(tb.tabulate(self.lst, header, tablefmt='pretty', showindex=True))


x0, y0, h0, dest = 0, 1, 0.02, 0.1
fun = lambda x, y: (y - x) / (y + x)
Euler(fun).Euler_Method(x0, y0, h0, dest)

# x0, y0, h0, dest = 0, 1, 0.1, 0.3
# fun = lambda x, y: (x ** 3 + x * y ** 2) * sp.exp(-1 * x)
# Euler(fun).Euler_Method(x0, y0, h0, dest)

# x0, y0, h0, dest = 0, 1, 0.1, 0.4
# fun = lambda x, y: x + sp.sin(y)
# Euler(fun).Euler_Method(x0, y0, h0, dest)

# x0, y0, h0, dest = 0, 1, 0.02, 0.1
# fun = lambda x, y: x + y
# Euler(fun).Euler_Method(x0, y0, h0, dest)

# x0, y0, h0, dest = 0, 2, 0.1, 0.4
# fun = lambda x, y: -1 * x * y ** 2
# Euler(fun).Modified_Euler(x0, y0, h0, dest)

# x0, y0, h0, dest = 0, 1, 0.1, 0.3
# fun = lambda x, y: (x ** 3 + x * y ** 2) * sp.exp(-1 * x)
# Euler(fun).Modified_Euler(x0, y0, h0, dest)

# x0, y0, h0, dest = 0, 1, 0.02, 0.04
# fun = lambda x, y: x ** 2 + y
# Euler(fun).Modified_Euler(x0, y0, h0, dest)

# x0, y0, h0, dest = 1, 2, 0.2, 1.4
# fun = lambda x, y: sp.ln(x + y)
# Euler(fun).Modified_Euler(x0, y0, h0, dest)
