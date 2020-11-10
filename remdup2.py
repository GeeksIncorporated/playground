class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        c = 0
        i = len(A) - 1
        while i >= 1:
            print(i)
            if A[i] == A[i - 1]:
                c += 1
            else:
                c = 0

            if c > 1:
                del A[i]
            i -= 1
        return A



s = Solution()
print(s.removeDuplicates([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]))
