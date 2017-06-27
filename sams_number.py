import sys

path = []
n = 0


def solve(s, m, d):
    global n

    if s == 0:
        if not path:
            return
        mins = min(path + [sys.maxint])
        maxs = max(path + [0])

        if maxs - mins <= d:
            n += 1
            print n, path
        return

    if s < 0:
        return

    for i in xrange(1, m + 1):
        if s < i:
            break

        path.append(i)
        solve(s - i, m, d)
        path.pop()


# Return the number of lists satisfying the conditions above, modulo 1000000009.
s, m, d = 20, 10, 5
solve(s, m, d)
print(n)