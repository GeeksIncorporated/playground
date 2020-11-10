# https://www.interviewbit.com/problems/min-xor-value/
# Given an array of N integers, find the pair of integers in the array which
# have minimum XOR value. Report the minimum XOR value.
#
# Examples :
# Input
# 0 2 5 7
# Output
# 2 (0 XOR 2)
# Input
# 0 4 7 9
# Output
# 3 (4 XOR 7)
#
# Constraints:
# 2 <= N <= 100 000
# 0 <= A[i] <= 1 000 000 000
#
# NOTE: You only need to implement the given function. Do not read input,
# instead use the arguments to the function. Do not print the output,
# instead return values as specified. Still have a doubt?
# Checkout Sample Codes for more details.

class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        min_x = 1000000000
        A = sorted(A)
        for i in range(1, len(A)):
            min_x = min(A[i] ^ A[i - 1], min_x)
        return min_x


s = Solution()
print((s.findMinXor([0, 2, 5, 7])))
