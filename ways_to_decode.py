# https://www.interviewbit.com/problems/ways-to-decode/
# Ways to Decode
#
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# Example :
#
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.


import string


class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        codes = dict(zip(map(str, range(1, 27)), string.ascii_uppercase))

        def solve(A):
            if not A:
                return 1
            r = 0
            for i in range(len(A)):
                word = A[:i + 1]
                if word in codes:
                    r += solve(A[i + 1:])
                else:
                    break
            return r

        return solve(A)


s = Solution()
assert s.numDecodings("12") == 2
assert s.numDecodings("123") == 3
assert s.numDecodings("17601") == 0
# assert s.numDecodings("17641839875689512341234123") == 4
print(s.numDecodings("17641839875689512341234123"))

