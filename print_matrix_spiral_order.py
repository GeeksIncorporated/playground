

# In
#
# 1 2 3
# 4 5 6
# 7 8 9
#
# Out
#
# 1 2 3 6 9 8 7 4 5

def submatrix(arr):
    res = []
    for i in range(1, len(arr) - 1):
        row = []
        for j in range(1, len(arr) - 1):
            row.append(arr[i][j])
        res.append(row)
    return res

def print_spiral_order(arr):

    n = len(arr) - 1
    if n == 0:
        print arr[0][0]
        return

    for i in range(n):
        print arr[0][i],

    for i in range(n):
        print arr[i][n],

    for i in range(n, 0, -1):
        print arr[n][i],

    for i in range(n, 0, -1):
        print arr[i][0],

    return print_spiral_order(submatrix(arr))

arr = [[1,2,3],[4,5,6],[7,8,9]]
assert submatrix(arr) == [[5]]
print_spiral_order(arr)