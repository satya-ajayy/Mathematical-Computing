import numpy as np

array1 = [[1, -3, 2], [4, 4, -1], [6, 3, 5]]
array2 = [[1], [0], [0]]
a = np.matrix(array1)
b = np.matrix(array2)

# a = np.matrix(np.zeros((3, 3), dtype='int'))
# b = np.matrix(np.zeros((3, 1), dtype='int'))

# print('For Matrix a ---> ')
# for i in range(3):
#     for j in range(3):
#         a[i, j] = int(input('Enter a[{}][{}] : '.format(i, j)))

# print('For Matrix b ---> ')
# for i in range(3):
#     for j in range(1):
#         b[i, j] = int(input('Enter b[{}][{}] : '.format(i, j)))

for i in range(10):
    print('Iteration -', i+1)
    c = a * b
    print('Eigen Value {:.3f}:'.format(np.abs(c).max()))
    print('Eigen Vector :\n', c)
    c = c / np.abs(c).max()
    c = np.round(c, decimals=3)
    print('Eigen Vector :\n', c)
    b = c
    print('-------------------')

print(np.linalg.eig(a)[0])
