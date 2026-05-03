"""Maximum depth of binary tree"""
class TreeNode:
    """class TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        """Function init"""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """class Solution"""
    def maxDepth(self, root: TreeNode) -> int:
        """Function finds maximum depth"""
        if not root:
            return 0

        max_depth = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)

                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))

        return max_depth
