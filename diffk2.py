
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer

    def bs(self, A, B):
        l = 0
        r = len(A)
        max_runs = int(r ** 0.5) + 1
        for _ in xrange(max_runs):
            m = (l + r) / 2
            if A[m] < B:
                l = m
            elif A[m] > B:
                r = m
            else:
                return m

    def diffPossible(self, A, B):
        A = sorted(A)
        for i in xrange(len(A)):
            r = self.bs(A, B + A[i])
            if r and r != i:
                return 1
        return 0

sol = Solution()
A = map(int, "16 36 29 4 45 80 86 53 37 39 78 40 80 64 44 35 73 48 64 82 46 97 75 26 83 20 9 23 2 20 74 96 78 27 28 68 99 5 24 98 26 56 40 26 93 97 93 82 40 46 13 11 25 9 20 39 79 45 65 76 31".split(" "))
print sol.diffPossible(A, 67)