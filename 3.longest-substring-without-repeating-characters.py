# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Given a string s, find the length of the longest substring without repeating characters.
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
import gc

class Solution(object):
    
    def __init__(self):
        gc.disable()
    
    def lengthOfLongestSubstring(self, s):
        window = set()
        l = r = 0
        max_len = 0
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            r += 1
            max_len = max(r-l, max_len)
        return max_len
        
# @lc code=end
