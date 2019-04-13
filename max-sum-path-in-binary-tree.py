# Definition for a  binary tree node
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

MAX_SUM = -1 << 32

class Solution:
    # @param A : root node of tree
    # @return an integer

    T = None

    def build_binary_tree_from_level_order(self, A):
        q = Queue()
        self.T = TreeNode(A[0])
        q.put(self.T)
        i = 0
        while not q.empty():
            node = q.get()
            i += 1
            if i < len(A):
                node.left = TreeNode(A[i])
                q.put(node.left)
            i += 1

            if i < len(A):
                node.right = TreeNode(A[i])
                q.put(node.right)

    def maxPathSum(self, A):

        def solve(A):
            global MAX_SUM

            if not A:
                return -1 << 32

            # leaf
            if not A.left and not A.right:
                return A.val

            lt = solve(A.left)
            rt = solve(A.right)
            MAX_SUM = max(MAX_SUM, A.val, lt, rt, lt+A.val, rt+A.val, lt + rt + A.val)
            return max(lt, rt) + A.val

        solve(A)
        return MAX_SUM


T = "3 2 -1 -1"
s = Solution()
s.build_binary_tree_from_level_order(
    list(map(int, T.split(' ')))
)

print(s.maxPathSum(s.T))

