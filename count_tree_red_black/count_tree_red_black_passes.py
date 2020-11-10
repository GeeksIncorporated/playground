import os
import sys
import time
from queue import Queue
from collections import defaultdict
sys.setrecursionlimit(100000)


class Solution:
    def __init__(self, n, c, w):
        self.P = {1: 0}  # parents
        self.T = defaultdict(lambda: [])

        self.W = {}  # weights
        self.E = defaultdict(lambda: [])  # Edges
        self.C = dict(list(zip(list(range(1, n + 1)), list(map(int, c.split(" "))))))  # Colors

        for line in w:
            u, v, w = line.strip().split(' ')
            u, v, w = [int(u), int(v), int(w)]
            # Write Your Code Here
            self.E[u].append(v)
            self.E[v].append(u)
            self.W[tuple(sorted((u, v)))] = w

        self.SUBTREE_BR_COUNTERS = {}

    def build_rooted_tree(self, root):
        """
        BFS-like approach to build rooted tree, stating from root.
        This fixes the E table (directions)
        """
        q = Queue()
        q.put(root)
        visited = set()
        visited.add(root)
        while not q.empty():
            node = q.get()
            for child in self.E[node]:
                if child in visited:
                    continue
                visited.add(child)
                self.T[node].append(child)
                self.P[child] = node
                q.put(child)

    def init_RB_counters(self, root):
        """
        :param root: 
        """

        def count_subtree(node):
            if self.T[node] == []:  # we are at leaf node
                if self.C[node] == 0:
                    return (1, 0)  # set BR counter
                else:
                    return (0, 1)  # set BR counter

            subtree_r = subtree_b = 0
            for child in self.T[node]:
                r, b = count_subtree(child)
                self.SUBTREE_BR_COUNTERS[child] = (r, b)
                subtree_r += r
                subtree_b += b

            if self.C[node] == 0:
                subtree_r += 1
            else:
                subtree_b += 1

            self.SUBTREE_BR_COUNTERS[node] = (subtree_r, subtree_b)
            return (subtree_r, subtree_b)

        count_subtree(root)

    def solve(self):
        total = 0
        self.build_rooted_tree(1)
        self.init_RB_counters(1)
        for i in range(len(self.C), 1, -1):
            Rr, Br = self.SUBTREE_BR_COUNTERS[1]  # Red, Black counters in all tree started from root
            Ri, Bi = self.SUBTREE_BR_COUNTERS[i]  # Red, Black counters in subtree rooted at i

            # The number of pathes through the edge is calculated as the cross
            # multiplication of edge weight with deltas of
            # R, B counters of whole the trees (Rr,Br) and the subtree (Ri,Bi).
            total += ((Rr - Ri) * Bi + (Br - Bi) * Ri) * self.W[tuple(sorted((self.P[i], i)))]

        return total


if __name__ == '__main__':

    for filename in os.listdir("datasets"):

        with open(os.path.join("datasets", filename)) as f:
            n = int(f.readline())
            expected_result = int(f.readline())
            c = f.readline()
            w = []
            for i in range(n):
                line = f.readline()
                if not line:
                    continue
                w.append(line)
            s = Solution(n, c, w)
            st = time.time()
            res = s.solve()
            assert res == expected_result, "Got invalid result with test: %s" % filename
            print("Ok:", filename, n, "entries took:", time.time() - st, "Res:", res)