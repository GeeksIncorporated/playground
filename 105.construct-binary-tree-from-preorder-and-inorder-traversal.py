#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # [5, 3, 1, 4, 7, 6, 5, 8, 9]
        #                    5
        #                3        7
        #            1     4    6   8
        #
        # Preorder:  5, 3, 1, 4, 7, 6, 8
        # Inorder:   1, 3, 4, 5, 6, 7, 8
        # Postorder: 1, 4, 3, 6, 8, 7, 5
        
        stack = []
        i = j = 0
        
        while preorder[i] != inorder[j]:
            stack.append(preorder[i])
            i += 1
        
            
            
            
        
        

# @lc code=end