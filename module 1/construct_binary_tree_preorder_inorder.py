"""Construct binary tree from preorder and inorder traversal"""
class TreeNode:
    """class TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        """Function init"""

        self.val = val
        self.left = left
        self.right = right

class Solution:
    """class Solution"""
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """Function build tree"""
        io_map = {}
        for i, value in enumerate(inorder): # переписала через enumerate
            io_map[value] = i

        return self.splitTree(preorder, io_map, 0, 0, len(inorder) - 1)

    def splitTree(self, preorder, io_map, rootIndex, left, right):
        """Function split tree"""
        if left > right:
            return None

        root = TreeNode(preorder[rootIndex])
        mid = io_map[preorder[rootIndex]]

        if mid > left:
            root.left = self.splitTree(preorder, io_map, rootIndex + 1, left, mid - 1)

        if mid < right:
            root.right = self.splitTree(preorder, io_map,
rootIndex + mid - left + 1, mid + 1, right)

        return root
