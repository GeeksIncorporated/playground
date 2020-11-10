from collections import defaultdict

#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        M = defaultdict(int)
        M[(-1, 0)] = 1
        for i in range(m):
            for j in range(n):
                M[(i, j)] = M[(i-1, j)] + M[(i, j-1)]
        return M[(m-1, n-1)]


# @lc code=end
