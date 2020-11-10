#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
import json
sys.setrecursionlimit(100000)

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Inorder traversal should do the job
        
        self.k = k
        
        def solve(root):
            
            if not root:
                return
            
            left = solve(root.left)
            
            self.k -= 1
            if self.k == 1:
                return root.val
            
            right = solve(root.right)
            return left or right
            
        return solve(root)
        
# @lc code=end
from queue import Queue

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


A = json.loads("[31,30,48,3,null,38,49,0,16,35,47,null,null,null,2,15,27,33,37,39,null,1,null,5,null,22,28,32,34,36,null,null,43,null,null,4,11,19,23,null,29,null,null,null,null,null,null,40,46,null,null,7,14,17,21,null,26,null,null,null,41,44,null,6,10,13,null,null,18,20,null,25,null,null,42,null,45,null,null,8,null,12,null,null,null,null,null,24,null,null,null,null,null,null,9]")


def built_bst(A):
    
    root = TreeNode(A[0])
    q = Queue()
    q.put((1, root))
    i = 0
    while not q.empty():
        i, node = q.get()
        
        if 2 * i + 1 < len(A):
            node.left = TreeNode(A[2 * i + 1])
        
        if 2 * 
        node.right = TreeNode(A[2 * i + 2])

        q.put((2 * i, node.left))
        q.put((2 * i + 1, node.right))
    
    return root

root = built_bst(A)
s = Solution()
print(s.kthSmallest(root, 0))