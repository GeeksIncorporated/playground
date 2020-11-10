
class Solution:

    def solve(self, A, s):
        start = 0
        curr_sum = 0
        for i in range(len(A)):
            curr_sum += A[i]
    
            while curr_sum > s and start < i:
                curr_sum -= A[start]
                start += 1

            if curr_sum == s:
                return [start, i]

        return -1


A = [7, 1, -5, 0, 2, 3, 1]
s = Solution()
assert s.solve(A, 0) == [2, 5]

