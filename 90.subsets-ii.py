#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        CACHE = {}
        res = set()
        combination = []
        def solve(nums):
            t = tuple(sorted(combination[::]))
            if nums == []:
                res.add(t)
                return True
            
            if t in CACHE:
                return CACHE[t]
            
            for i in range(len(nums)):
                combination.append(nums[i])
                solve(nums[:i] + nums[i+1:])
                combination.pop()
                solve(nums[:i] + nums[i+1:])
            
            CACHE[t] = res
            
        solve(nums)
        return res
        
# @lc code=end

