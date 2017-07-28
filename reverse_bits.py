# https://www.interviewbit.com/problems/reverse-bits/

# Reverse bits of an 32 bit unsigned integer
#
# Example 1:
#
# x = 0,
#
#           00000000000000000000000000000000
# =>        00000000000000000000000000000000
#
# return 0
#
# Example 2:
#
# x = 3,
#
#           00000000000000000000000000000011
# =>        11000000000000000000000000000000
#
# return 3221225472
#
# Since java does not have unsigned int, use long
from math import log


class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        B = 0
        while A:
            lsb = int(log(A & ~(A - 1), 2))  # get least significant bit
            B |= (1 << 31 - lsb)
            A &= (A - 1)  # drop least signinficant bit
        return B


s = Solution()
assert s.reverse(3) == 3221225472