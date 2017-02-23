import pprint

import numpy as np

print np.random.randint(5, size=(5, 5))

M1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

M3 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]

M2 = [[1, 1, 1, 4, 4],
      [0, 0, 3, 0, 4],
      [0, 0, 0, 2, 2],
      [1, 0, 4, 1, 0],
      [4, 1, 2, 0, 1]]


def switch(M, point1, point2):
    M[point1[0]][point1[1]], M[point2[0]][point2[1]] = M[point2[0]][point2[1]], M[point1[0]][point1[1]]
    return M


def submatrix(M):
    res = []
    N = len(M)
    for i in range(1, N - 1):
        row = []
        for j in range(1, N - 1):
            row.append(M[i][j])
        res.append(row)
    return res


def rotate(M):
    N = len(M) - 1
    if len(M) <= 1:
        return M

    for i in range(N):
        M = switch(M, [i, 0], [N, i])

    for i in range(N):
        M = switch(M, [N, i], [N - i, N])

    for i in range(N):
        M = switch(M, [N - i, N], [0, N - i])

    MP = rotate(submatrix(M))
    for i in range(len(MP)):
        for j in range(len(MP)):
            M[i + 1][j + 1] = MP[i][j]

    return M


pprint.pprint(M3)
rotate(M3)
print
pprint.pprint(M3)
