#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        def __solve(p,q):
            
            if not p and not q:
                return True
            elif not p or not q:
                return False

            if p.val != q.val:
                return False

            return all([
                solve(p.left, q.left),
                solve(p.right, q.right)])

        def solve(p,q):
            stuck = [(p,q)]
            while stuck:
                p,q = stuck.pop()
                
                if not q and not p:
                    continue

                elif not q or not p:
                    return False

                if p.val != q.val:
                    return False
                
                stuck.append((p.left, q.left))
                stuck.append((p.right,q.right))
            return True

        return solve(p,q)

