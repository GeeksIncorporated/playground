class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list

    def get_cycle_length(self, slow, fast):
        length = 1
        slow = slow.__next__
        while slow != fast:
            slow = slow.__next__
            length += 1
        return length

    def detectCycle(self, A):

        if not A or not A.__next__:
            return None

        slow = fast = A
        fast = fast.__next__
        while slow:
            print(slow, fast)
            if slow == fast:
                cycle_length = self.get_cycle_length(slow, fast)
                print("--", cycle_length)
                slow = fast = A
                for i in range(cycle_length):
                    fast = fast.__next__
                while slow != fast:
                    slow = slow.__next__
                    fast = fast.__next__
                return slow

            slow = slow.__next__

            if fast.__next__ and fast.next.__next__:
                fast = fast.next.__next__
            else:
                return

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)

s = Solution()
input = list(map(int, "1 2 3 4 5 2".split(' ')))


nodes = {}
st = prev = Node(input[0])
nodes[str(st)] = st

for i in range(1, len(input)):
    if str(input[i]) in nodes:
        next = nodes[str(input[i])]
    else:
        next = Node(input[i])
        nodes[str(next)] = next
    print("--X", prev, next)
    prev.next = next
    prev = next

print(s.detectCycle(st))
