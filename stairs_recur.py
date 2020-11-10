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
import sys
sys.setrecursionlimit(100000)


class Solution:
    # @param A : integer
    # @return an integer
    cache = {}

    def climbStairs(self, n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n in self.cache:
            return self.cache[n]
        r = 0
        r += self.climbStairs(n - 1)
        r += self.climbStairs(n - 2)
        self.cache[n] = r
        return r


import time

s = Solution()
st = time.time()
print((s.climbStairs(30)))
print((time.time() - st))
