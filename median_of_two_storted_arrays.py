# https://www.interviewbit.com/problems/median-of-array/
# Median of Array
#
# There are two sorted arrays A and B of size m and n respectively.
#
# Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).
#
# The overall run time complexity should be O(log (m+n)).
#
# Sample Input
#
# A : [1 4 5]
# B : [2 3]
#
# Sample Output
#
# 3
#
#     NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element.
#     For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double

    def median(self, arr):
        l = len(arr)
        if l == 1:
            return arr[0], 0
        if l % 2:
            return arr[l / 2], l / 2
        else:
            return (arr[l / 2 - 1] + arr[l / 2]) / 2.0, l / 2

    def findMedianSortedArrays(self, A, B):

        if not A:
            return self.median(B)[0]

        if not B:
            return self.median(A)[0]

        if len(A) < 3 and len(B) < 3:
            return (max(A[0], B[0]) + min(A[-1], B[-1])) / 2.0

        m1, m1_ind = self.median(A)
        m2, m2_ind = self.median(B)

        if m1 < m2:
            if len(A) % 2 == 0:
                m1_ind -= 1
            return self.findMedianSortedArrays(A[m1_ind:], B[:m2_ind+1])

        elif m1 > m2:
            if len(A) % 2 == 0:
                m2_ind -= 1
            return self.findMedianSortedArrays(A[:m1_ind+1], B[m2_ind:])
        else:
            return A[m1_ind]


s = Solution()

# print s.findMedianSortedArrays([], [20])
print s.findMedianSortedArrays([1, 4, 5], [2, 3])
# print s.findMedianSortedArrays(
#     [-50, -41, -40, -19, 5, 21, 28],
#     [-50, -21, -10])

print s.findMedianSortedArrays(
    [-50, -47, -36, -35, 0, 13, 14, 16],
    [-31, 1, 9, 23, 30, 39])
