from collections import defaultdict
import time

class Solution:

    def is_valid(self, s):
        counter = 0
        for c in s:
            if c == '(':
                counter += 1
            elif c == ")":
                counter -= 1
            if counter < 1:
                return False
        return counter == 0

    def minRemoveToMakeValid(self, s):

        def solve(s, k):
            # D(s) = 1 + min(D(s[:i]) + D(s[i+1:]) for i in range(len(s)))

            if self.is_valid(s):
                yield 0, [k]

            solutions = defaultdict(lambda: [])
            min_removes = 1000000

            for i in range(len(s)):
                if s[i] == '(' or s[i] == ')':
                    for l, lindeces in solve(s[:i], k):
                        for r, rindeces in solve(s[i + 1:], k):
                            removes = 1 + l + r
                            if removes <= min_removes:
                                min_removes = removes
                                solutions[removes].append(
                                    (removes, lindeces + rindeces))

        return solve(s, 0)


s = Solution()
st = time.time()
r = s.minRemoveToMakeValid("(()")
for s in r:
    print(list(s))
print(time.time() - st)
print(r)
