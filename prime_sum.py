import math


class Solution:
    # @param A : integeri
    # @return a list of integers

    def isprime(self, n):
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def primesum(self, A):
        for i in xrange(2, A):
            if self.isprime(i) and self.isprime(A - i):
                return i, A - i

s = Solution()
print s.primesum(4)