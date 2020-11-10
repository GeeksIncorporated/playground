#
# @lc app=leetcode id=449 lang=python
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json

try:
    from queue import Queue
except:
    from Queue import Queue

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        res = []
        def solve(root):
            if not root:
                res.append(json.dumps(None))
                return None
            res.append(root.val)
            if root.left or root.right:
                solve(root.left)
                solve(root.right)
            return res
        return json.dumps(solve(root))


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        A = json.loads(data)
        if not A:
            return None
        def solve(A):
            i = 0
            root = TreeNode(A[0])
            q = Queue()
            q.put(root)
            for i in range(len(A) // 2):
                node = q.get()
                left = 2 * i + 1
                right = 2 * i + 2
                node.left = TreeNode(A[left])
                node.right = TreeNode(A[right])
                q.put(node.left)
                q.put(node.right)
            return root
        return solve(A)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

s = Codec()
r = s.deserialize("[3,1,4,null,2]")
r = s.serialize(r)
r = s.deserialize(r)
print(s.serialize(r))

