import itertools
import random
import sys
from collections import defaultdict

import math

import time


def subarrays(l):
    res = set()
    print(l)
    for size in range(len(l)+1):
        print(size)
        for q in zip(*(l[i:] for i in range(size))):
            res.add(q)
    return res


def inc_subsequences(l):
    res = set()
    i = 0
    while i < (1 << len(l)):
        j = i
        i += 1
        repr = []
        while j:
            lsb = j & ~(j - 1)                      # get least segnificant bit value which equal to 2**key
            key = int(math.log(lsb, 2))             # get the key from previous
            if key > 0 and l[key] < l[key - 1]:
                print((l, key, l[key], l[key - 1]))
                break
            repr.append(l[key])
            j &= j - 1
        res.add(tuple(repr))
    return res


def inc_subsequences1(l):
    res = set()
    for size in range(1, len(l) + 1):
        for c in itertools.combinations(l, size):
            if sorted(c) == list(c):
                res.add(c)
    return res


a = tuple([random.randint(0, 100) for i in range(4)])

st = time.time()
r = subarrays(a)
print((time.time() - st))
print((len(r)))
print(r)

# st = time.time()
# r = inc_subsequences(a)
# print r
# print time.time() - st
# print len(r)
#
# st = time.time()
# r = inc_subsequences1(a)
# print r
# print time.time() - st
# print len(r)
# l = (2, 3, 1)
# subrays = subarrays(l)
# m_mins = defaultdict(list)
# fl_max = -sys.maxint
# count = 0
# for a in subarrays(l):
#     inc_sum = -sys.maxint
#     for seq in inc_subsequences(a):
#         s = sum(seq)
#         if inc_sum < s:
#             inc_sum = s
#
#     fl = sum(a) - inc_sum
#     if fl_max < fl:
#         fl_max = fl
#         if len(a) <= m_mins[fl_max]:
#             m_mins[fl_max] = len(a)
#             if a[-1] - a[0] + 1 == len(a):
#                 count += 1
