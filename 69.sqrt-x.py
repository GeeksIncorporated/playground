#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 0
        r = x  
        
        if x == 0:
            return 0

        if x < 4:
            return 1

        m = l + (r - l) // 2
        res = m ** 2

        while not (x - 0.5 <= res <= x + 0.5):
            m = l + (r - l) // 2
            res = m ** 2
            print(res)
            if res > x:
                r = m - 0.5
            elif res < x:
                l = m + 0.5

        return int(m)

# @lc code=end

