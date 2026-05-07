"""Kth smallest element in a BST"""
class TreeNode:
    """class TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        """Function init"""
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """class Solution"""
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """Function kth smallest"""
        io_list = []
        self.helper(root, io_list)

        return io_list[k - 1]

    def helper(self, tree_node, io_list):
        """Function helper"""

        if tree_node is None:
            return

        self.helper(tree_node.left, io_list)
        io_list.append(tree_node.val)
        self.helper(tree_node.right, io_list)
