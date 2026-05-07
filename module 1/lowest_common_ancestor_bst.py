"""Lowest common ancestor of a binary search tree"""
class TreeNode:
    """class TreeNode"""
    def __init__(self, x):
        """Function init"""
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """class Solution"""
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode
    ) -> TreeNode:
        """Function lowest common ancestor"""

        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right

            elif p.val < root.val and q.val < root.val:
                root = root.left

            else:
                return root
