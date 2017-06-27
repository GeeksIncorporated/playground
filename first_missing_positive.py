class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        sA = set(A)
        candidate = 1
        while True:
            if candidate not in sA:
                return candidate
            candidate += 1

s = Solution()
assert s.firstMissingPositive([1, 2, 0]) == 3
