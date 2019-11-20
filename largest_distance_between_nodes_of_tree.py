# Find largest distance
# Given an arbitrary unweighted rooted tree which consists
# of N (2 <= N <= 40000) nodes. The goal of the problem is to find largest
# distance between two nodes in a tree. Distance between two nodes is a number
# of edges on a path between the nodes (there will be a unique path between
# any pair of nodes since it is a tree). The nodes will be
# numbered 0 through N - 1.
#
# The tree is given as an array P, there is an edge between nodes P[i]
# and i (0 <= i < N). Exactly one of the i’s will have P[i] equal to -1,
# it will be root node.
#
#     Example:
#     If given P is [-1, 0, 0, 0, 3], then node 0 is the root and the
#       whole tree looks like this:
#
#           0
#        /  |  \
#       1   2   3
#                \
#                 4
#
#     One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3,
# thus the answer is 3. Note that there are other paths with maximal distance.


import sys
sys.setrecursionlimit(50000)
from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @return an integer

    def __init__(self):
        self.local_max_distance = 0
        self.global_max_distance = 0
        self.tree = defaultdict(lambda: list())

    def build_tree(self, A):
        for i, a in enumerate(A):
            if a == -1:
                continue
            self.tree[a].append(i)

    def dfs(self, node):
        maxes = [0, 0]
        first_max, second_max = 0, 0
        for child in self.tree[node]:
            h = self.dfs(child)
            maxes.append(h)
            maxes = sorted(maxes, reverse=True)[:2]

        self.local_max_distance = sum(maxes)
        self.global_max_distance = max(self.global_max_distance,
                                       self.local_max_distance)
        return maxes[0] + 1

    def solve(self, A):
        self.build_tree(A)
        self.dfs(0)
        return self.global_max_distance



A = [-1, 0, 1, 1, 3, 0, 4, 0, 2, 8, 9, 0, 4, 6, 12, 14, 7, 9, 6, 4, 14, 13, 1,
     9, 16, 17, 17, 0, 21, 10, 13, 14, 25, 28, 27, 0, 35, 20, 34, 23, 37, 3, 6,
     25, 30, 22, 15, 37, 8, 6, 11, 22, 50, 12, 4, 2, 54, 23, 18, 52, 34, 49,
     61, 8, 15, 63, 31, 51, 48, 41, 26, 37, 30, 15, 59, 12, 0, 40, 37, 73, 32,
     19, 70, 29, 8, 21, 83, 33, 7, 13, 12, 82, 43, 86, 38, 31, 1, 84, 62, 83]
s = Solution()
print(s.solve(A))
