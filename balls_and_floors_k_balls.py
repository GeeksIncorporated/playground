import sys
sys.setrecursionlimit(2000)

N = 1000
cache = {}

def solve(floors,k):
    if k < 2 or  len(floors) < 2:
        return len(floors)

    if (len(floors),k) in cache:
        return cache[(len(floors),k)]

    min_res = sys.maxint
    for i in range(len(floors)):
        res = max(solve(floors[i + 1:], k), solve(floors[:i],k-1))
        if min_res > res:
            min_res = res
            f = floors[i]
    cache[(len(floors),k)] = min_res + 1
    return min_res + 1


print i, solve(range(1, i + 1), 4)