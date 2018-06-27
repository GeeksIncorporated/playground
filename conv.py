
import pprint
from collections import defaultdict

import time


def build_mask(x, y):
    mask = ['0' * 9] * 9
    for i in range(9):
        mask[i] = format(1 << (8 - y), '09b')

    block_i = x // 3
    block_j = y // 3
    for i in range(3):
        for j in range(3):
            mask[3 * block_i + i] = format(7 << (6 - 3 * block_j), '09b')
    mask[x] = '1' * 9
    return mask


masks = defaultdict(list)

for i in range(9):
    for j in range(9):
        masks[(i, j)] = ''.join(build_mask(i, j))

pprint.pprint(masks)

N = 9
board = "404046000060000009000000000002000000000000000003060020100000900800005000000000005"
board = [list(map(int, list(line))) for line in
         [board[i:i + N] for i in range(0, len(board), N)]]

number_masks = [format(0, "081b")] * 10

st = time.time()
for i in range(9):
    for j in range(9):
        n = board[i][j]
        if not n:
            continue
        n_mask = format(1 << (81 - (9 * i + j + 1)), "081b")
        x = int(number_masks[n], 2) ^ int(n_mask, 2)
        number_masks[n] = format(x, "081b")


print(">>>> ", time.time() - st)



def print_b(b):
    print()
    for n in range(9):
        print(b[9*n:9*n + 9])




