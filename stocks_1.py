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

import sys


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        profit = 0
        curr_min = A[0]
        for a in A:
            curr_min = min(curr_min, a)
            profit = max(profit, a - curr_min)
        return profit


s = Solution()
A = [3, -1, 2, 1, 2]
print s.maxProfit(A)
