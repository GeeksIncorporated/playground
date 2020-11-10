"""
Generators which return al permutations and
permutations with predefined length.
"""

import time


def perms(A):
    if len(A) == 2:
        yield A
        yield [A[1], A[0]]
    else:
        for i in range(len(A)):
            for p in perms(A[:i] + A[i + 1:]):
                yield [A[i]] + p


def perms_with_length(A, l):
    if l == 1:
        for a in A:
            yield [a]
    else:
        for i in range(len(A)):
            for p in perms_with_length(
                    A[:i] + A[i + 1:],
                    l - 1):
                yield [A[i]] + p


st = time.time()
# for p in perms(range(8)):
#     print p

t1 = time.time()
for p in perms_with_length([0], 1):
    print(p)

print(t1 - st)
print(time.time() - t1)
