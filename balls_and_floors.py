import sys
sys.setrecursionlimit(2000)

N = 1000
cache = {}


def solve(floors):
    if len(floors) < 2:
        return len(floors)

    if str(floors) in cache:
        return cache[str(floors)]

    min_res = sys.maxint
    for i in range(min(len(floors), 15)):
        res = max(solve(floors[i + 1:]), i)
        if min_res > res:
            min_res = res

    cache[str(floors)] = min_res + 1
    return min_res + 1


tries = solve(range(1, N + 1))
print "Floors", N
print "Max tries", tries
