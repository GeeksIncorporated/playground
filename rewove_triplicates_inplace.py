
# TODO: solve this
class Solution:
    # @param A : list of integers
    # @return an integer

    def get_next_wanted(self):
        n = yield
        yield n
        yield n

    def removeDuplicates(self, A):
        j = 0
        i = 0
        while i < len(A) - 1:
            if A[i] != A[i+1] or A[i] != A[i+2]:
                j += 1
                if A[i] <


A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
s = Solution()
# print s.removeDuplicates(A)
print s.removeDuplicates([0, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5])
