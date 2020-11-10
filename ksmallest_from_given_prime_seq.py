import heapq
import sys
sys.setrecursionlimit(2048)

class Solution():
    res = 1
    factors = []
    ksmallest = []
    cache = set()

    def solve(self, primes, k):
        primes = sorted(primes)

        def dfs(root, depth):
            self.factors.append(root)

            self.res *= root
            if depth < 2:
                return

            if self.res in self.cache:
                return

            if -self.res not in self.ksmallest:
                if len(self.ksmallest) >= k:
                    heapq.heappushpop(
                        self.ksmallest, -self.res)
                else:
                    heapq.heappush(
                        self.ksmallest, -self.res)
            l = len(primes)
            for i in range(l):
                dfs(primes[i], depth - 1)
                last = self.factors.pop()
                self.res /= last
                self.cache.add(self.res)

        dfs(1, k + 1)
        return sorted(set(
            ([int(-x) for x in self.ksmallest])))[1:k + 1]

primes = (3, 5, 7)
s = Solution()
print((s.solve(primes, 30)))
