import sys
import time
import heapq

import math

c = 0
h = []
maxp = 0
problem = 0
maxage = 120


def gettriple(n):
    s1 = min(maxage, int(math.sqrt(n)) + 1)
    for n1 in xrange(1, s1):
        if n % n1 == 0:
            res = n / n1
            s2 = min(maxage, int(math.sqrt(n)) + 1)
            for n2 in xrange(1, s2):
                if res % n2 == 0:
                    n3 = int(res / n2)
                    if n3 > maxage:
                        continue
                    yield (n1, n2, n3)


def solve(n):
    triples = set()
    for triple in gettriple(n):
        triples.add(tuple(sorted(triple)))
    return sorted(triples)


def isgood(triple):
    return triple[1] != triple[2]


def main(n):
    from collections import defaultdict
    sums = defaultdict(lambda: list())

    for t in solve(n):
        sums[sum(t)].append(t)

    for k, v in sums.items():
        if len(v) > 1:
            for t in v:
                if isgood(t):
                    yield v, len(sums)


st = time.time()
for s1 in xrange(1, maxage):
    for s2 in xrange(s1, maxage):
        i = s1 * s2 * s2
        l = list(main(i))
        if len(l) == 1:
            if (s1, s2, s2) not in l[0][0]:
                continue
            c += 1
            print '\r', l
            sys.stdout.flush()
            res = l[0][1]
            if len(h) <= 100:
                heapq.heappush(h, (res, l, i))
            else:
                heapq.heappushpop(h, (res, l, i))

while h:
    r = heapq.heappop(h)
    print r

print c, time.time() - st
