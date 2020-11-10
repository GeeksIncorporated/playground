import decimal
import time
import sys
sys.setrecursionlimit(10000000)


def isprime(n):
    # print('isprime', n)
    l = int(decimal.Decimal(n).sqrt())
    for i in range(2, l + 1):
        if n % i == 0:
            return False
    return True


def prime_factorize(n):
    factors = []

    def solve(n, factors):
        n = int(n)
        if isprime(n):
            return sorted(factors+[n])

        for i in range(2, n // 2 + 1):
            if n % i == 0 and isprime(i):
                factors.append(i)
                res = solve(n // i, factors)
                if res:
                    return res
                factors.pop()
        return factors

    return solve(n, factors)


# N = 2 ** 20
# while N > 0:
#     if isprime(N):
#         print(N)
#     N -= 1

N = 100000001
st = time.time()
print(N, prime_factorize(N), flush=True)
print(time.time() - st)

# print('\r', end='', flush=True)
