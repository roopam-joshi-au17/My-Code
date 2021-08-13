'''
Q-3) Same Tree (5 marks)
https://leetcode.com/problems/same-tree/
Given the roots of two binary trees p and q, write a function to check if they
are the same or not.
Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        elif p is None and q is None:
            return True
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)