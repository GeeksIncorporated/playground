
from collections import defaultdict
import time


def build_cross_mask(x, y):
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
        masks[(i, j)] = ''.join(build_cross_mask(i, j))

for k, v in masks.items():
    print(k, v)

N = 9
board = "400006000" \
        "060000009" \
        "000000000" \
        "002000000" \
        "000000000" \
        "003060020" \
        "100000900" \
        "800005000" \
        "000000005"
board = [list(map(int, list(line))) for line in
         [board[i:i + N] for i in range(0, len(board), N)]]

number_masks = [format(0, "081b")] * 10

# build number_masks
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
print(masks[(1, 0)])
print(number_masks[6])

# Get minimum cell candidates
st = time.time()
cands = defaultdict(list)
min_cands_cell = (10, 0, 0, [])
for i in range(9):
    for j in range(9):
        cands[(i,j)] = [n for n in range(1, 10) if int(masks[(i, j)], 2) & int(number_masks[n], 2) == 0]
        if len(cands[(i,j)]) < min_cands_cell[0]:
            min_cands_cell = (len(cands[(i,j)]), i, j, cands[(i,j)])
print(time.time() - st)
print(min_cands_cell)

