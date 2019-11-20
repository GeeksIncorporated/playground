from copy import copy


class Solution:
    res = []

    def avgset(self, A):
        A = sorted(A)
        avg = sum(A) / len(A)
        l = []
        res = []

        def solve(m):
            if m == 0:
                if l and float(sum(l)) / len(l) == avg:
                    res.append(copy(l))


            l.append(A[m])
            solve(m - 1)
            l.pop()
            solve(m - 1)

        solve(len(A) - 1)
        return res

s = Solution()
# print s.avgset([1, 7, 15, 29, 11, 9])
print s.avgset([1, 2, 3])
