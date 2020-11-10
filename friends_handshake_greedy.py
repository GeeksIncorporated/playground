import itertools
from pprint import pprint
import constraint

CACHE = set()
PAIRS = list(zip(list(range(0, 10, 2)), list(range(1, 10, 2))))
PAIRS += list([(p[1], p[0]) for p in PAIRS])
TABLE = None


def fill_table_with_zeros():
    global TABLE
    TABLE = [[0 for i in range(10)] for j in range(10)]


def get_upper_matrix_indeces():
    pr = constraint.Problem()
    pr.addVariables('ij', list(range(10)))
    pr.addConstraint(lambda i, j: i < j)
    pr.addConstraint(lambda i, j: (i, j) not in PAIRS)
    res = []
    for s in pr.getSolutions():
        TABLE[s['i']][s['j']] = 1
        res.append((s['i'], s['j']))
    print("Since the handshakes are symetric, "
          "we are going to work with upper matrix, marked as 1s")
    pprint(TABLE)
    return res


def all_columns_sum_differs():
    global MAX_SO_FAR, TABLE

    sums = []
    for i in range(10):
        sums.append(sum(TABLE[i]))
    print(("", sums, MAX_SO_FAR))
    ss = len(set(sums))
    p = MAX_SO_FAR
    MAX_SO_FAR = max(MAX_SO_FAR, ss)
    if p != MAX_SO_FAR:
        print((MAX_SO_FAR, ss))
        pprint(TABLE)
    return ss == 9


def total_number_of_handshakes_matchs():
    s = 0
    for pair in UPPER_MATRIX_INDECES:
        s += TABLE[pair[0]][pair[1]]
    print(s)
    return 13 < s < 23


def solve(column, num_of_handshakes_to_make):
    # pprint(TABLE)
    # print()
    if num_of_handshakes_to_make < 0:
        if all_columns_sum_differs():
            print("DONE!")
            return True
        return False

    s = [1] * num_of_handshakes_to_make + [0] * (8 - num_of_handshakes_to_make)

    for perm in list(set(itertools.permutations(s, 8))):
        j = 0
        for i in range(10):
            if i != column and (i, column) not in PAIRS:
                TABLE[i][column] = perm[j]
                TABLE[column][i] = perm[j]
                j += 1
                # pprint(TABLE)

        if solve(column - 1, num_of_handshakes_to_make - 1):
            return True

        TABLE[column] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


fill_table_with_zeros()
MAX_SO_FAR = 0
UPPER_MATRIX_INDECES = get_upper_matrix_indeces()
fill_table_with_zeros()
solve(8, 8)
