# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/
# Remove Duplicates from Sorted Array
#
# Remove duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
#
# Note that even though we want you to return the new length, make sure to change the original array as well in place
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
#     Example:
#     Given input array A = [1,1,2],
#     Your function should return length = 2, and A is now [1,2].



class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        # Base case
        if len(A) <= 1:
            return len(A)

        i = j = 0
        prev = A[0]
        while i < len(A) and j < len(A):
            # advancing j to the next bigger element than prev
            if A[j] <= prev:
                j += 1
                continue
            # if the distance from current A[i] to the next bigger A[j] is more
            # than 1, we should switch A[i+1] with the A[j] to preserve sorted order of A
            if j - i > 1:
                i += 1
                A[i], A[j] = A[j], A[i]
            else:
                i += 1
            # udpate prev
            prev = A[i]
        # the length of the sorted portion of A is i+1
        return i + 1


s = Solution()
A = [0, 1, 1, 2, 2, 3, 3, 3, 3]
assert s.removeDuplicates(A) == 4
