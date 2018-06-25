import pprint
from collections import defaultdict


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
        masks[(i,j)] = ''.join(build_mask(i, j))

pprint.pprint(masks)

