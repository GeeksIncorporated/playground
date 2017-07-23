# https://codelab.interviewbit.com/problems/combinations/

# Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.
#
# Make sure the combinations are sorted.
#
# To elaborate,
# 1. Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
# 2. Entries should be sorted within themselves.
#
# Example :
# If n = 4 and k = 2, a solution is:
#
# [
#   [1,2],
#   [1,3],
#   [1,4],
#   [2,3],
#   [2,4],
#   [3,4],
# ]
#
#     Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
#     Example : itertools.combinations in python.
#     If you do, we will disqualify your submission retroactively and give you penalty points.
#


from copy import copy


class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
    def combine(self, n, k):
        self.combinations = []
        self.curr_combination = []

        def solve(n, k):
            if n < 0:
                return

            if k == 0:
                self.combinations.append(sorted(copy(self.curr_combination)))
                return

            self.curr_combination.append(n)
            solve(n - 1, k - 1)
            self.curr_combination.pop()
            solve(n - 1, k)

        solve(n, k)
        return sorted(self.combinations)


s = Solution()
print s.combine(10, 2)