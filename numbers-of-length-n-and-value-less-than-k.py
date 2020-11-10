# https://www.interviewbit.com/problems/numbers-of-length-n-and-value-less-than-k/
# Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.
#     NOTE: All numbers can only have digits from the given set.
# Examples:
# 	Input:
# 	  3 0 1 5
# 	  1
# 	  2
# 	Output:
# 	  2 (0 and 1 are possible)
# 	Input:
# 	  4 0 1 2 5
# 	  2
# 	  21
# 	Output:
# 	  5 (10, 11, 12, 15, 20 are possible)
# Constraints:
#     1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9
#


class Solution:
    def getDigits(self, x):
        digits = []
        while x:
            digits.append(x % 10)
            x = x // 10
        if len(digits) == 0:
            digits.append(0)
        digits.reverse()
        return digits

    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if len(A) == 0:
            return 0

        digits = self.getDigits(C)
        smaller = [0] * 10
        exists = [0] * 10

        for i in A:
            exists[i] = smaller[i] = 1
        for i in range(1, 10):
            smaller[i] += smaller[i - 1]

        if B > len(digits):
            return 0
        if B < len(digits):
            result = smaller[9] - smaller[0]
            if B == 1:
                result += smaller[0]
            for i in range(2, B + 1):
                result *= smaller[9]
            return result

        if B == 1:
            return smaller[C]
        if smaller[digits[0]] == 0:
            return 0
        result = (smaller[digits[0] - 1] - smaller[0]) * (len(A) ** (B - 1))
        for i in range(1, B):
            if exists[digits[i - 1]] == 0:
                break
            result += (smaller[digits[i]] - exists[digits[i]]) * (len(A) ** (B - i - 1))
        return result


s = Solution()
print(s.solve([0, 1, 2, 3, 4, 5, 7, 8, 9],
              5,
              51822))
