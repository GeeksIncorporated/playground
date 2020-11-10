import math
import time

subs = []

# recursive approach
def solve(A):
    if not A:
        print(subs)
        return

    subs.append(A[-1])
    solve(A[:-1])

    subs.pop()
    solve(A[:-1])

# binary array representation approach
def solve1(A):
    l = len(A)
    upper = 1 << l

    def get_next_lsb(n):
        """
        iterator over least significant bits
        for 1000101 will return 1,3,7
        :param n: 
        """
        while n:
            lsb = int(math.log(n & ~(n - 1), 2))
            n ^= 1 << lsb
            yield lsb

    for i in range(upper):
        print([A[lsb] for lsb in get_next_lsb(i)])


A = list(range(15))

st = time.time()
solve(A)
t1 = time.time() - st
print()
st = time.time()
solve1(A)
print(t1, time.time() - st)
