

# https://codelab.interviewbit.com/problems/addnum/
# ADDNUM
#
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
#     342 + 465 = 807
#
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        C = ListNode(0)
        rC = C
        res = 0
        while A or B or res:
            a = A.val if A else 0
            b = B.val if B else 0
            s = a + b + res
            C.val = s % 10
            res = s / 10
            A = A.next if A else None
            B = B.next if B else None
            if A or B or res:
                C.next = ListNode(0)
                C = C.next

        return rC

L1 = ListNode(2)
L1.next = ListNode(4)
L1.next.next = ListNode(3)
L2 = ListNode(5)
L2.next = ListNode(6)
L2.next.next = ListNode(4)

s = Solution()
L3 = s.addTwoNumbers(L1, L2)
while L3:
    print L3.val, "->",
    L3 = L3.next
print "NULL"