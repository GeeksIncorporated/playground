# https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram/0
# Find the largest rectangular area possible in a given histogram where the
# largest rectangle can be made of a number of contiguous bars.
# For simplicity, assume that all bars have same width and the width is 1 unit.
#
# Input:
# The first line contains an integer 'T' denoting the total number of test cases.
# T test-cases follow. In each test cases, the first line contains an integer 'N'
# denoting the size of array.
# The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array. The elements of the array represents the height of the bars.
#
# Output:
# For each test-case, in a separate line, the maximum rectangular area possible
# from the contiguous bars.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 103
# 1 <= A[i] <= 1018
#
# Example:
# Input:
# 1
# 7
# 6 2 5 4 5 1 6
# Output:
# 12
# This solution is in O(nlogn)
# There is a solution at Geeks4Geeks in O(n)
# But this is way more compact and readable ;)

import random
import time


class Solution:
    counter = 0

    def find_min(self, A):
        mi = 0
        mv = 1000
        for i in range(len(A)):
            Solution.counter += 1
            if A[i] < mv:
                mv = A[i]
                mi = i
        return mi

    def solve(self, A):
        """
        The problem is solved Dynamically: it may be subtracted to smaller
        problems which optimal sulution will give an optimal solution to the
        original problem.
        Find min bar, then either 3 of options are possible:
        min bar heigh * len(A) is the max rectangle
        the subproblem from the left will give a max rectangle
        the subproblem from the right will give a max rectange
        :param A:
        :return:
        """
        if not A:
            return 0

        if len(A) == 1:
            return A[0]

        m = self.find_min(A)
        return max([
            A[m] * len(A),
            self.solve(A[:m]),
            self.solve(A[m + 1:])
        ])


solution = Solution()
st = time.time()
for i in range(1, 1000):
    A = [random.choice(list(range(100))) for i in range(i)]
    Solution.counter = 0
    r = solution.solve(A)
    print((r, Solution.counter, Solution.counter / int(r)))
print((time.time() - st))

A = [6, 2, 5, 4, 5, 20, 6, 4, 3]
Solution.counter = 0
r = solution.solve(A)
print((r, Solution.counter, Solution.counter / int(r)))
