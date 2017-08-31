import math


def isprime(n):
    if n <= 3:
        return True

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def primefactorization(n):
    res = []

    def solve(n):
        if n <= 2:
            return True

        for k in range(2, n + 1):
            if n % k == 0 and isprime(k):
                res.append(k)
                if solve(int(n / k)):
                    return True

    solve(n)
    return res


res = []
for i in range(10000):
    pf = primefactorization(i)
    res.append((len(pf), pf, i))

print(list(reversed(sorted(res))))
