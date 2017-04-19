import bisect

import sys

a = [28, 33, 95, 63, 33, 35, 83, 29, 84, 99]


def find_lis(arr):
    M = [1] + [sys.maxint] * len(arr)
    for i in range(len(arr)):
        bisect.insort_right(M, arr[i])
    return len(M)

# assert(bs(range(100), 10), 10)

print find_lis(a)
