#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        res = []
        while x:
            res.append(x%10)
            x = x // 10
        return res == list(reversed(res))


# @lc code=end

