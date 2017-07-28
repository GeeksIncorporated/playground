# https://www.interviewbit.com/problems/prettyprint/
# Print concentric rectangular pattern in a 2d matrix.
# Let us show you some examples to clarify what we mean.
#
# Example 1:
#
# Input: A = 4.
# Output:
#
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4
#
# Example 2:
#
# Input: A = 3.
# Output:
#
# 3 3 3 3 3
# 3 2 2 2 3
# 3 2 1 2 3
# 3 2 2 2 3
# 3 3 3 3 3
#
# The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.
#
# You will be given A as an argument to the function you need to implement, and you need to return a 2D array.

from pprint import pprint


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):

        # M is going to be a 2d zeros array with size 2Ax2A
        M = map(list, ((0,) * (2 * A - 1),) * (2 * A - 1))

        A -= 1

        # Going to fill the M by quarter
        # 1:1
        for x in xrange(A + 1, -1, -1):
            for i in xrange(x):
                M[A + i][A + x - 1] = x

            for j in xrange(x):
                M[A + x - 1][A + j] = x

        # 1:-1
        for x in xrange(A + 1, -1, -1):
            for i in xrange(x):
                M[A + i][A - (x - 1)] = x

            for j in xrange(x):
                M[A + x - 1][A - j] = x

        # -1:1
        for x in xrange(A + 1, -1, -1):
            for i in xrange(x):
                M[A - i][A + x - 1] = x

            for j in xrange(x):
                M[A][A + j] = x
                M[A - (x - 1)][A + j] = x

        # -1:-1
        for x in xrange(A + 1, -1, -1):
            for i in xrange(x):
                M[A - i][A - (x - 1)] = x

            for j in xrange(x):
                M[A - (x - 1)][A - j] = x

        return M


s = Solution()
pprint(s.prettyPrint(9))
