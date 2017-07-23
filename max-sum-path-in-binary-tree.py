# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue


class Solution:
    # @param A : root node of tree
    # @return an integer

    def lca(self, parents, n1, n2):
        path1 = []
        path2 = []
        while n1:
            path1.append(n1)
            n1 = parents[n1]

        while n2:
            path2.append(n2)
            n2 = parents[n2]

        return list(set(path1).intersection(set(path2)))[-1]

    def maxPathSum(self, A):

        parents = {A: None}
        path_sum = {}

        q = []
        q.append(A)
        path_sum[A] = A.val

        while q:
            node = q.pop()

            if node.left:
                parents[node.left] = node
                path_sum[node.left] = path_sum[node] + node.left.val
                q.append(node.left)

            if node.right:
                parents[node.right] = node
                path_sum[node.right] = path_sum[node] + node.right.val
                q.append(node.right)

        print path_sum
        max_ps = -1000000
        nodes = parents.keys()
        for i, node1 in enumerate(nodes):
            for node2 in nodes[i:]:
                if node1 == node2:
                    ps = node1.val
                else:
                    lca = self.lca(parents, node1, node2)
                    ps = path_sum[node1] + path_sum[node2] - 2 * lca.val
                if ps > max_ps:
                    max_ps = ps
        return max_ps


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


root = Node(-100)
q = Queue()
q.put(root)
root.left = Node(-200)
root.right = Node(-300)
root.left.left = Node(-400)
# for i in xrange(1, 10, 2):
#     node = q.get()
#     node.left = Node(i + 1)
#     node.right = Node(i + 2)
#     q.put(node.left)
#     q.put(node.right)

s = Solution()
print s.maxPathSum(root)
