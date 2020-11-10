
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers

    def bs_from_side(self, A, B, side):
        l = 0
        r = len(A)
        for i in range(int(len(A) ** 0.5) + 1):
            m = (l + r) / 2
            if A[m] < B:
                l = m
            elif A[m] > B:
                r = m
            else:
                if side == "left":
                    if m == 0 or A[m - 1] < B:
                        return m
                    r = m
                if side == "right":
                    if m == len(A) - 1 or A[m + 1] > B:
                        return m
                    l = m
        return -1

    def searchRange(self, A, B):
        return self.bs_from_side(A, B, "left"), self.bs_from_side(A, B,"right")

s = Solution()

A = list(map(int, "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10".split(" ")))
B = 2
print(s.searchRange(A, B))

A, B = [1, 1], 1
assert s.searchRange(A, B) == (0, 1)

A, B = [1,2,3,3,3, 4,5,6,7,8,9,10], 3
assert s.searchRange(A, B) == (2, 4)

A, B = [1] * 100, 3
assert s.searchRange(A, B) == (-1, -1)