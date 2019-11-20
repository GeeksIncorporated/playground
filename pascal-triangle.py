# https://www.interviewbit.com/problems/pascal-triangle/
#
# Given numRows, generate the first numRows of Pascal’s triangle.
#
# Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
#
# Example:
#
# Given numRows = 5,
#
# Return
#
# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]

from collections import defaultdict
from pprint import pprint


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A == 0:
            return 0

        T = [[1] + [0] * A]
        res = [[1]]
        for i in range(1, A):
            raw = []
            for j in range(A):
                raw.append(T[i - 1][j - 1] + T[i - 1][j])
            res.append(raw[:i+1])
            T.append(raw)
        return res

s  = Solution()
pprint(s.solve(5))