#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#
from itertools import combinations
# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return combinations(range(1,n+1), k)
        
        
# @lc code=end

