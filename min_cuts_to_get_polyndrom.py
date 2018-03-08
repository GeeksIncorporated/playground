# https://www.interviewbit.com/problems/palindrome-partitioning-ii/
# Palindrome Partitioning II
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example :
# Given
# s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


class Solution:
    # @param A : string
    # @return an integer

    def is_palindrome(self, A):
        return A == A[::-1]

    def minCut(self, A):
        cache = {}

        def solve(i):
            if i in cache:
                return cache[i]

            if i == len(A) or \
                self.is_palindrome(A[i:]):
                min_cuts = 0
            else:
                min_cuts = len(A)
                for j in xrange(i + 1, len(A)):
                    word = A[i:j]
                    if self.is_palindrome(word):
                        min_cuts = min(min_cuts, 1 + solve(j))
            cache[i] = min_cuts
            return min_cuts

        return solve(0)


A = "bbabab"
s = Solution()
assert s.minCut(A) == 1

A = "ababb"
s = Solution()
assert s.minCut(A) == 1

A = "XfCtL38GNmYvAhmYEIecokbWJjAXsdGZ3Ro1dT1BEx6fFGPqmMMaRAaYcPFvcobsNtWZxW1U" \
    "11kEHfRbMpv2q3VGPVOP8dK"
s = Solution()
assert s.minCut(A) == 91
