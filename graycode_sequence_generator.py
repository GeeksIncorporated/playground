# https://codelab.interviewbit.com/problems/graycode/
#
# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
#
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# There might be multiple gray code sequences possible for a given n.
# Return any such sequence.

# Warning this is working but not inefficient solution.

import sys
sys.setrecursionlimit(100000)


class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        self.result = [0]
        self.seen_codes = set([0])

        def solve(code, A):
            for i in range(A):
                t = code ^ (1 << i)
                if t in self.seen_codes:
                    continue
                code = t
                self.seen_codes.add(code)
                self.result.append(code)
                solve(code, A)

        solve(0, A)
        return tuple(self.result)

s = Solution()
print(s.grayCode(10))

# There is a dirty trick:
#
# The bruteforce method would be to start with 0, change any of the bits, keeping track of the numbers already constructed. When you run into a number where there is no way forward possible, you backtrack, and try to change some other bit instead.
# This might however be inefficient.
#
# Note the following :
#
# Let G(n) represent a gray code of n bits.
# Note that reverse of G(n) is also a valid sequence.
# Let R(n) denote the reverse of G(n).
#
# Note that we can construct
# G(n+1) as the following :
# 0G(n)
# 1R(n)
#
# Where 0G(n) means all elements of G(n) prefixed with 0 bit and 1R(n) means all elements of R(n) prefixed with 1.
# Note that last element of G(n) and first element of R(n) is same. So the above sequence is valid.
#
# Example G(2) to G(3) :
# 0 00
# 0 01
# 0 11
# 0 10
# 1 10
# 1 11
# 1 01
# 1 00
