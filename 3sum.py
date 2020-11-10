# https://www.interviewbit.com/problems/3-sum/
# Given an array S of n integers, find
# three integers in S such that the sum
# is closest to a given number, target.
# Return the sum of the three integers.
#
# Assume that there will only be one
# solution
#
# Example:
# given array S = {-1 2 1 -4},
# and target = 1.
#
# The sum that is closest to the target
# is 2. (-1 + 2 + 1 = 2)
import sys


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def twoSumClosest(self, A, B):
        l = 0
        r = len(A) - 1
        while l < r - 1:
            s = A[l] + A[r]
            if s > B:
                r -= 1
            elif s < B:
                l += 1
            else:
                break
        return A[l], A[r]

    def threeSumClosest(self, A, B):
        res = []
        A = sorted(A)
        closest = sys.maxsize
        res = 0
        for i, a in enumerate(A):
            e1, e2 = self.twoSumClosest(
                A[:i] + A[i + 1:],
                B - a)
            if closest > abs(B - (
                    a + e1 + e2)):
                closest = abs(
                    B - (a + e1 + e2))
                res = a + e1 + e2
                if closest == 0:
                    break
        return res


A = [-5, 1, 4, -7, 10, -7, 0, 7, 3, 0,
     -2, -5, -3, -6, 4, -7, -8, 0, 4,
     9, 4, 1, -8, -6, -6, 0, -9, 5, 3,
     -9, -5, -9, 6,
     3, 8, -10, 1, -2, 2, 1, -9, 2,
     -3, 9, 9, -10, 0, -9, -2, 7, 0,
     -4, -3, 1, 6, -3]
B = -1
s = Solution()
print(s.threeSumClosest(A, B))

A = [-1, 2, 1, -4]
B = 1
print(s.threeSumClosest(A, B))
