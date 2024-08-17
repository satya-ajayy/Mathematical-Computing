import math as m


def normal(matrix):
    x1 = m.sqrt(matrix[0][0] ** 2 + matrix[1][0] ** 2 + matrix[2][0] ** 2)
    x2 = m.sqrt(matrix[0][1] ** 2 + matrix[1][1] ** 2 + matrix[2][1] ** 2)
    x3 = m.sqrt(matrix[0][2] ** 2 + matrix[1][2] ** 2 + matrix[2][2] ** 2)
    matrix[0][0] = matrix[0][0] / x1
    matrix[1][0] = matrix[1][0] / x1
    matrix[2][0] = matrix[2][0] / x1
    matrix[0][1] = matrix[0][1] / x2
    matrix[1][1] = matrix[1][1] / x2
    matrix[2][1] = matrix[2][1] / x2
    matrix[0][2] = matrix[0][2] / x3
    matrix[1][2] = matrix[1][2] / x3
    matrix[2][2] = matrix[2][2] / x3
    return matrix


def gcd(first, middle, last):
    return m.gcd(first, middle, last)


def determinant(matrix):
    first = matrix[0][0] * ((matrix[2][2] * matrix[1][1]) - (matrix[2][1] * matrix[1][2]))
    middle = matrix[0][1] * ((matrix[2][2] * matrix[1][0]) - (matrix[2][0] * matrix[1][2]))
    last = matrix[0][2] * ((matrix[2][1] * matrix[1][0]) - (matrix[2][0] * matrix[1][1]))
    det = first - middle + last
    return det


def change(matrix):
    list1 = [matrix[0][0], matrix[1][0], matrix[2][0]]
    list2 = [matrix[0][1], matrix[1][1], matrix[2][1]]
    list3 = [matrix[0][2], matrix[1][2], matrix[2][2]]
    lst = [list1, list2, list3]
    return lst


def mul(matrix1, matrix2):
    matrix3 = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matrix3[i][j] = matrix3[i][j] + matrix1[i][k] * matrix2[k][j]
    return matrix3


def transpose(matrix1):
    matrix2 = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            matrix2[i][j] = matrix1[j][i]
    return matrix2


def modify(lst1):
    lst = []
    k = None
    for i in lst1:
        if i != 0:
            lst.append(i)
    if len(lst) == 1:
        k = gcd(abs(lst[0]), abs(lst[0]), abs(lst[0]))
    if len(lst) == 2:
        k = gcd(abs(lst[0]), abs(lst[1]), abs(lst[0]))
    if len(lst) == 3:
        k = gcd(abs(lst[0]), abs(lst[1]), abs(lst[2]))
    for i in range(len(lst1)):
        lst1[i] = lst1[i] / k
    return lst1


def eigen_vector(matrix, l):
    lst = [[0 for _ in range(3)] for _ in range(3)]
    I = [[l, 0, 0], [0, l, 0], [0, 0, l]]
    list1 = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            lst[i][j] = matrix[i][j] - I[i][j]
    print("eigen matrix for lambda", l, "is:", lst)
    for x1 in range(-49, 49):
        for x2 in range(-49, 49):
            for x3 in range(-49, 49):
                if (x1 * lst[0][0] + x2 * lst[0][1] + x3 * lst[0][2] == 0
                        and x1 * lst[1][0] + x2 * lst[1][1] + x3 * lst[1][2] == 0
                        and x1 * lst[2][0] + x2 * lst[2][1] + x3 * lst[2][2] == 0):
                    list1 = [x1, x2, x3]
                    break
    list2 = modify(list1)
    print("eigen vector for lambda", l, "is;", "{}i+{}j+{}k".format(*list2))
    return list2


A = [[0 for i in range(3)] for j in range(3)]
cubic_roots = []
for i in range(3):
    for j in range(3):
        print("Enter A[", i, "][", j, "]", end=" ")
        A[i][j] = int(input(":"))
s1 = 0
for i in range(3):
    s1 += A[i][i]
print("trace:", s1)
p = A[1][1] * A[2][2] - A[2][1] * A[1][2]
q = A[2][2] * A[0][0] - A[2][0] * A[0][2]
r = A[1][1] * A[0][0] - A[1][0] * A[0][1]
s2 = p + q + r
print("sum of minors:", s2)
x = A[0][0] * ((A[2][2] * A[1][1]) - (A[2][1] * A[1][2]))
y = A[0][1] * ((A[2][2] * A[1][0]) - (A[2][0] * A[1][2]))
z = A[0][2] * ((A[2][1] * A[1][0]) - (A[2][0] * A[1][1]))
s3 = x - y + z
print("Determinant is:", s3)
# eqn=a**3-s1*a**2+s2*a-s3
# eqn1=3*a**2-2*s1*a=s2
for a in range(-99, 99):
    if a ** 3 - s1 * a ** 2 + s2 * a - s3 == 0:
        cubic_roots.append(a)
print("roots are:", cubic_roots)
b = []
for i in range(len(cubic_roots)):
    l1 = eigen_vector(A, cubic_roots[i])
    b.append(l1)
print("normal matrix:", b)
c = change(b)
print("modal matrix:", c)
n = normal(c)
print("normalised matrix:", n)
nt = transpose(n)
print("transpose matrix:", nt)
M = mul(nt, A)
L = mul(M, n)
print(f"diagonal eigen vector:{round(L[0][0])}i+{round(L[1][1])}j+{round(L[2][2])}k")
