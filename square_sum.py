import os
os.getcwd()


class Solution(object):

    def is_perfect(self, n):
        sq = n ** 0.5
        return n == int(sq) ** 2

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = [1] * n
        combination = []
        cache = {}

        def solve(n):

            if n in cache:
                return cache[n]

            if n == 0:
                # print(combination)
                if len(combination) < len(self.res):
                    self.res = combination[:]
                    print(combination)
                return True

            if n < 0:
                return False
            
            i = 1
            while i**2 <= n:
                combination.append(i**2)
                solve(n - i**2)
                combination.pop()
                i += 1
            cache[n] = self.res
        solve(n)
        return len(self.res)


s = Solution()
s.numSquares(48)
print(s.res)
