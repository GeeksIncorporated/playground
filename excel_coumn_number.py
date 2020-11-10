class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        # A -> 1
        # B -> 2
        # C -> 3
        # Z -> 26
        # AA -> 27
        # AB -> 28
        n = 0
        for c in A:
            n = 26 * n + ord(c) - 64
        return n

s = Solution()
print(s.titleToNumber('AB'))