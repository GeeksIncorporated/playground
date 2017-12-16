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
        min_so_far = 1000000000000
        profit = 0
        for a in A:
            if a < min_so_far:
                min_so_far = a
            profit = max(profit, a - min_so_far)
        return profit

s = Solution()
A = [int(100 * math.sin(x)) for x in range(1000000)]
assert s.maxProfit(A) == 198
