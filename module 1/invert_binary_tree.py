"""Invert Binary Tree"""

class TreeNode:
    """class TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        """Function init"""
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """class Solution"""
    def invertTree(self, root: TreeNode) -> TreeNode:
        """Function inverts Tree"""
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
