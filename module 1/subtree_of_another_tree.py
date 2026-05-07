"""Subtree of another tree"""
class TreeNode:
    """class TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        """Function init"""
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """class Solution"""
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        """Function is subtree"""

        if subRoot is None:
            return True

        if root is None and subRoot is not None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        left_check = self.isSubtree(root.left, subRoot)
        right_check = self.isSubtree(root.right, subRoot)

        return left_check or right_check

    def isSameTree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        """Function is same"""

        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        if root.val != subRoot.val:
            return False

        return (
            self.isSameTree(root.left, subRoot.left)
            and self.isSameTree(root.right, subRoot.right)
        )
