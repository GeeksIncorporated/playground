#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
from collections import defaultdict

# @lc code=start
class Solution:

    def show(self, M, n):
        for i in range(n):
            row = []
            for j in range(n):
                row.append(M[(i,j)])
            print(row)
        print("----------------")

    def generateMatrix(self, n: int):
        c = 1
        N = n
        M = defaultdict(int)
        i, j = 0, 0
        while c <= N**2:

            if c == N ** 2:
                M[(i, j)] = c
                break

            while j < n-1:
                M[(i, j)] = c
                c += 1
                j += 1
                
            while i < n-1:    
                M[(i, j)] = c
                c += 1
                i += 1
                
            while j > N-n:
                M[(i, j)] = c
                c += 1
                j -= 1
                
            while i > N-n:
                M[(i, j)] = c
                c += 1
                i -= 1
                
            i += 1
            j += 1
            n -= 1
            
            
        res = []
        for i in range(N):
            row = []
            for j in range(N):
                row.append(M[(i,j)])
            res.append(row)
        return res

# @lc code=end

s = Solution()
s.generateMatrix(1)