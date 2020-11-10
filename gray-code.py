from copy import copy


class Solution(object):

    def solve(self, A, i):
        print(A)

        if i == len(A):
            return

        A[i] = 1
        self.solve(copy(A), i+1)


s = Solution()
r = s.solve([0,] * 4, 0)