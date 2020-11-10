# https://codelab.interviewbit.com/problems/subset2/
#
# Given a collection of integers that might contain duplicates, S, return all possible subsets.
#
#     Note:
#
#         Elements in a subset must be in non-descending order.
#         The solution set must not contain duplicate subsets.
#         The subsets must be sorted lexicographically.
#
# Example :
# If S = [1,2,2], the solution is:
#
# [
# [],
# [1],
# [1,2],
# [1,2,2],
# [2],
# [2, 2]
# ]


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        self.seen_subsets = set()
        n = len(A) - 1
        self.subset = []

        def solve(A, n):
            if n < 0:
                self.seen_subsets.add(tuple(sorted(self.subset)))
                return
            self.subset.append(A[n])
            solve(A, n - 1)
            self.subset.pop()
            solve(A, n - 1)

        solve(A, n)
        return sorted(self.seen_subsets)


A = [1, 2, 2]
s = Solution()
for ss in s.subsetsWithDup(A):
    print(ss)

# The solution on the website seems much better:
#
#     NOTE : This is user generated solution and not an editorial solution
#
# class Solution:
#     def subsetsWithDup(self, A):
#         n = 2**len(A)
#         subsets = set()
#
#         A = sorted(A)
#
#         for i in xrange(n):
#             subset = []
#             for j, v in enumerate(A):
#                 if i & (1 << j):
#                     subset.append(v)
#             subsets.add(tuple(subset))
#
#         return sorted(subsets)
#
