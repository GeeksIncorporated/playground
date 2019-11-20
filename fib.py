

# To illustrate dynamic programming recursive
# approach:
import time

CACHE = {}
USE_CACHE = False


def fib(n):
    if n <= 3:
        return n
    if n in CACHE and USE_CACHE:
        return CACHE[n]
    res = fib(n-1) + fib(n-2)
    CACHE[n] = res
    return res

N = 50
USE_CACHE = True
st = time.time()
print(fib(N))
print(time.time() - st)

USE_CACHE = False
st = time.time()
print(fib(N))
print(time.time() - st)
