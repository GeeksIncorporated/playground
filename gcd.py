
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):

        if B == 0:
            return A

        while A > 0:
            A, B = B, abs(A - B)
        return B

s = Solution()
print s.gcd(18, 9)