# https://www.interviewbit.com/problems/square-root-of-integer/
# Square Root of Integer
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# If x is not a perfect square, return floor(sqrt(x))
#
# Example :
#
# Input : 11
# Output : 3
#
# DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
#

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if not A:
            return A
        l = 1
        r = A
        while r - l > 1:
            m = (l + r) / 2
            res = m ** 2
            if res > A:
                r = m
            elif res < A:
                l = m
            else:
                return m
        return l


s = Solution()
assert s.sqrt(0) == 0
assert s.sqrt(1) == 1
assert s.sqrt(5) == 2
assert s.sqrt(16) == 4
assert s.sqrt(258) == 16
assert s.sqrt(300) == 17
