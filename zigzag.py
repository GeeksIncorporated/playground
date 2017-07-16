from collections import defaultdict


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings

    def wave(self, n):
        while True:
            for i in xrange(n):
                yield i
            for i in xrange(n - 2, 0, -1):
                yield i

    def convert(self, A, B):
        stacks = defaultdict(lambda: [])
        wavy_iterator = self.wave(B)
        for c in A:
            i = wavy_iterator.next()
            stacks[i].append(c)
        res = []
        for i in xrange(len(stacks)):
            res.append("".join(stacks[i]))
        return "".join(res)


s = Solution()
print s.convert("B", 1)
