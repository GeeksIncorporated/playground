class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        A = A.strip(".0")
        B = B.strip(".0")
        n1 = map(int, A.split("."))
        n2 = map(int, B.split("."))
        if n1 > n2:
            return 1
        elif n1 < n2:
            return -1
        else:
            return 0

sol = Solution()
print sol.compareVersion("1.0", "1")
print sol.compareVersion("1.1", "1.2")
print sol.compareVersion("1.2", "1.13")
print sol.compareVersion("1.13", "1.13.4")
