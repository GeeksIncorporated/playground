# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-i/
#
# Best Time to Buy and Sell Stocks I
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example :
#
# Input : [1 2]
# Return :  1


import math


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        max_profit = 0
        maxs = self.precalculate_suffix_maxes(A)

        for i in xrange(len(A)):
            max_profit = max(maxs[i] - A[i], max_profit)
        return max_profit

    def precalculate_suffix_maxes(self, A):
        maxs = {}
        curr_max = 0
        for i in xrange(len(A) - 1, -1, -1):
            curr_max = max(A[i], curr_max)
            maxs[i] = curr_max
        return maxs


s = Solution()
A = [int(100 * math.sin(x)) for x in xrange(1000000)]
assert s.maxProfit(A) == 198
