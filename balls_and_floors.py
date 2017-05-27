import sys
sys.setrecursionlimit(2000)

N = 100
cache = {}

solution = set()
def solve(floors):
    if len(floors) < 2:
        return len(floors)

    if str(floors) in cache:
        return cache[str(floors)]

    min_res = sys.maxint
    for i in range(len(floors)):
        res = max(solve(floors[i + 1:]), i)
        if min_res > res:
            min_res = res
            f = floors[i]

    solution.add(f)
    cache[str(floors)] = min_res + 1
    return min_res + 1


tries = solve(range(1, N + 1))
print
print "Floors", N
print "Max tries", tries
print sorted(list(solution))