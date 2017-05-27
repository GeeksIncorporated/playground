#!/bin/python
import pprint
import sys
from data import n, c, w
sys.setrecursionlimit(10000000)
from collections import defaultdict

W = {}
E = defaultdict(lambda: [])
C = dict(zip(xrange(n), map(int, c.split(" "))))
for line in w:
    u, v, w = line.strip().split(' ')
    u, v, w = [int(u), int(v), int(w)]
    # Write Your Code Here
    E[u].append(v)
    E[v].append(u)
    W[tuple(sorted((u, v)))] = w

global_sum = 0
local_sum = 0
CACHE = {}


def dfs(root, curr_node):
    global local_sum, global_sum
    if C[curr_node - 1] == 1:
        global_sum += local_sum

    visited.add(curr_node)
    adjs = E[curr_node]
    for adj in adjs:
        if adj not in visited:
            w = W[tuple(sorted((curr_node, adj)))]
            local_sum += w
            k = tuple(sorted((root, adj)))
            if k in CACHE:
                print root, adj, CACHE[k], local_sum
            CACHE[k] = local_sum
            dfs(root, adj)
            local_sum -= w

dd = 0
for node, c in C.items():
    dd += 1
    visited = set()
    if C[node] == 0:
        dfs(node + 1, node + 1)
        with open("cache", "a+") as f:
            f.write(pprint.pformat(CACHE))
assert global_sum == 5672569099