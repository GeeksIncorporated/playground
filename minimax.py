class Solution:
    # @param A : list of integers
    # @return an integer

    def maxcoin(self, A, turn=1):
        if not A:
            return 0

        if len(A) == 1:
            return turn * A[0]

        #TODO:

s = Solution()
s.maxcoin([1, 2, 3, 4])
