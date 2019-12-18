
from pprint import pprint
import constraint

PAIRS = list(zip(range(0, 10, 2), range(1, 10, 2)))
PAIRS += list(map(lambda p: (p[1], p[0]), PAIRS))
TABLE = [[0 for i in range(10)] for j in range(10)]


def get_upper_matrix_indeces():
    pr = constraint.Problem()
    pr.addVariables('ij', range(10))
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


UPPER_MATRIX_INDECES = get_upper_matrix_indeces()

pr = constraint.Problem()
MAX_SO_FAR = 0
FULL_MATRIX = [[0 for i in range(10)] for i in range(10)]


def all_columns_sum_differs(*table_vals):
    global MAX_SO_FAR, FULL_MATRIX
    sums = []

    for p, val in enumerate(table_vals):
        i, j = UPPER_MATRIX_INDECES[p]
        FULL_MATRIX[i][j] = val
        FULL_MATRIX[j][i] = val

    for i in range(10):
        sums.append(sum(FULL_MATRIX[i]))

    ss = len(set(sums))
    p = MAX_SO_FAR
    MAX_SO_FAR = max(MAX_SO_FAR, ss)
    if p != MAX_SO_FAR:
        print(MAX_SO_FAR, ss)
        pprint(FULL_MATRIX)
    return ss == 9


def total_handshakes_num_smaller_than_22(*vals):
    return sum(vals) < 23


for pair in UPPER_MATRIX_INDECES:
    pr.addVariable(pair, [1, 0])


pr.addConstraint(total_handshakes_num_smaller_than_22)
pr.addConstraint(all_columns_sum_differs)

for s in pr.getSolutions():
    print(s)
