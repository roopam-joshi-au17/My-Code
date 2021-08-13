'''
Q-2 ) Lowest Common Ancestor of a Binary Search Tree (5
marks)
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search
-tree/
(Easy)
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest node in T that has both p and
q as descendants (where we allow a node to be a descendant of itself).”
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node1=p if p.val<q.val else q
        node2=q if q.val>p.val else p
        res= self.lcautil(root,node1,node2)
        return res
    
    def lcautil(self,root,node1,node2):
        if node1.val<=root.val and root.val<=node2.val:
            return root
        elif root.val>node1.val and root.val>node2.val:
            return self.lcautil(root.left,node1,node2)
        else:
            return self.lcautil(root.right,node1,node2)