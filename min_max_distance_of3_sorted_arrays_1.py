
# https://www.interviewbit.com/problems/minimize-the-absolute-difference/
# Given three sorted arrays A, B and Cof not necessarily same sizes.
#
# Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
# i.e. minimize | max(a,b,c) - min(a,b,c) |.
#
# Example :
#
# Input:
#
# A : [ 1, 4, 5, 8, 10 ]
# B : [ 6, 9, 15 ]
# C : [ 2, 3, 6, 6 ]
#
# Output:
#
# 1
#
# Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.


import sys


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        ind = dict(A=0, B=0, C=0)
        min_distance = sys.maxsize
        while ind["A"] < len(
            A) and ind["B"] < len(
            B) and ind["C"] < len(C):
            maximum = max(
                (A[ind["A"]], "A"),
                (B[ind["B"]], "B"),
                (C[ind["C"]], "C"))

            minimum = min(
                (A[ind["A"]], "A"),
                (B[ind["B"]], "B"),
                (C[ind["C"]], "C"))

            min_distance = min(abs(
                maximum[0] - minimum[
                    0]), min_distance)

            ind[minimum[1]] += 1
        return min_distance


A = [1, 4, 5, 8, 10]
B = [6, 9, 10]
C = [2, 3, 6, 10]
s = Solution()
print(s.solve(A, B, C))
