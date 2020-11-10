# https://www.interviewbit.com/problems/stairs/
# Stairs
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example :
#
# Input : 3
# Return : 3
#
# Steps : [1 1 1], [1 2], [2 1]


class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A == 0:
            return 0

        if A == 1:
            return 1

        prev1 = 1
        prev2 = 1
        curr = 2
        for i in range(1, A):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return curr

import time

s = Solution()
st = time.time()
print((s.climbStairs(30)))
print((time.time() - st))