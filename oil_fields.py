# https://www.interviewbit.com/problems/black-shapes/
# Given N * M field of O's and X's, where O=white, X=black
# Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)
#
# Example:
#
# OOOXOOO
# OOXXOXO
# OXOOOXO
#
# answer is 3 shapes are  :
# (i)    X
#      X X
# (ii)
#       X
#  (iii)
#       X
#       X
#
# Note that we are looking for connected shapes here.
#
# For example,
#
# XXX
# XXX
# XXX
#
# is just one single connected black shape.
#
#     NOTE: You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.

class Solution:
    # @param A : list of strings
    # @return an integer

    def __init__(self):
        self.visited = set()

    def get_adjs(self, node, A):
        x, y = node

        adjs = ((min(len(A) - 1, x + 1), y),
                (max(0, x - 1), y),
                (x, min(len(A[0]) - 1, y + 1)),
                (x, max(0, y - 1)))

        adjs = set([c for c in adjs if A[c[0]][c[1]] == "X"])
        adjs.discard(node)
        return adjs

    def visit(self, root, A):
        q = list()
        q.append(root)
        while q:
            node = q.pop()
            self.visited.add(node)
            for adj in self.get_adjs(node, A):
                if adj not in self.visited:
                    q.append(adj)

    def black(self, A):
        res = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == "X" and (i, j) not in self.visited:
                    res += 1
                    self.visit((i, j), A)
        return res


A = ["XOOOOOXXOX",
     "OOXXXXOOXX",
     "XXOXXOOXXO",
     "OXOXXXXXXO",
     "XOXXOXOXXX",
     "OOOOOOOXOO",
     "XOXXXOOXOX",
     "XXXOXOXXXO"]

s = Solution()
print((s.black(A)))
