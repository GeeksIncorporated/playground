import math

class Solution:

    # @param A : integer
    # @return an integer
    def reverse(self, A):
        res = 0
        positive = A > 0
        if not positive: A *= -1
        while A:
            res = 10 * res + A % 10
            A /= 10
        if not positive: res *= -1
        return res

sol = Solution()
print sol.reverse(123)