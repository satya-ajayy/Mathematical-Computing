r = int(input("enter rows:"))
c = int(input("enter columns:"))
A = [[0 for i in range(r)] for j in range(c)]
det = None
if r == c:
    if r == 1:
        for i in range(r):
            for j in range(c):
                print("Enter A[", i, "][", j, "]", end=" ")
                A[i][j] = int(input(":"))
                det = A[0][0]
        print("Determinant of given 1×1 Matrix is:", det)
    if r == 2:
        for i in range(r):
            for j in range(c):
                print("Enter A[", i, "][", j, "]", end=" ")
                A[i][j] = int(input(":"))
                det = A[1][1] * A[0][0] - A[1][0] * A[0][1]
        print("Determinant of given 2×2 Matrix is:", det)
    if r == 3:
        for i in range(r):
            for j in range(c):
                print("Enter A[", i, "][", j, "]", end=" ")
                A[i][j] = int(input(":"))
                x = A[0][0] * ((A[2][2] * A[1][1]) - (A[2][1] * A[1][2]))
                y = A[0][1] * ((A[2][2] * A[1][0]) - (A[2][0] * A[1][2]))
                z = A[0][2] * ((A[2][1] * A[1][0]) - (A[2][0] * A[1][1]))
                det = x - y + z
        print("Determinant of given 3×3 Matrix is:", det)
    if r > 3:
        print("Nake thelidhu\nThelisthe Cheppu")
else:
    print("Error..!!!\nDet is Only possible for square matrices Only where rows and columns are equal")
