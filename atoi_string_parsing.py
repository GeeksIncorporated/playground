# https://www.interviewbit.com/problems/atoi/
# Atoi
# Please Note:
#
# There are certain questions where the interviewer would intentionally frame the question vague.
# The expectation is that you will ask the correct set of clarifications or state your assumptions before you jump into coding.
#
# Implement atoi to convert a string to an integer.
#
# Example :
#
# Input : "9 2704"
# Output : 9
#
# Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.
#
#     Questions:
#
#     Q1. Does string contain whitespace characters before the number?
#     A. Yes
#
#     Q2. Can the string have garbage characters after the number?
#     A. Yes. Ignore it.
#
#     Q3. If no numeric character is found before encountering garbage characters, what should I do?
#     A. Return 0.
#
#     Q4. What if the integer overflows?
#     A. Return INT_MAX if the number is positive, INT_MIN otherwise.
#
# Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
# If you do, we will disqualify your submission retroactively and give you penalty points.

import sys


class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        res = 0
        sign = 1
        # the number may be either positive or negative
        if A[0] == "-":
            sign = -1
            A = A[1:]
        elif A[0] == "+":
            A = A[1:]

        # iterate through A till non numeric is found.
        # we indicate numeric as 48 <= ord(c) <= 57
        for c in A:
            o = ord(c) - 48
            if 0 <= o <= 9:
                res = 10 * res + o
            else:
                break
        # task requirements to bound the result by +-int32
        res = min(sign * res, 2147483647)
        return max(res, -2147483648)