class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list

    def get_cycle_length(self, slow, fast):
        length = 1
        slow = slow.next
        while slow != fast:
            slow = slow.next
            length += 1
        return length

    def detectCycle(self, A):

        if not A or not A.next:
            return None

        slow = fast = A
        fast = fast.next
        while slow:
            print slow, fast
            if slow == fast:
                cycle_length = self.get_cycle_length(slow, fast)
                print "--", cycle_length
                slow = fast = A
                for i in range(cycle_length):
                    fast = fast.next
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

            slow = slow.next

            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

s = Solution()
input = map(int, "1 2 3 4 5 2".split(' '))


nodes = {}
st = prev = Node(input[0])
nodes[str(st)] = st

for i in range(1, len(input)):
    if str(input[i]) in nodes:
        next = nodes[str(input[i])]
    else:
        next = Node(input[i])
        nodes[str(next)] = next
    print "--X", prev, next
    prev.next = next
    prev = next

print s.detectCycle(st)
