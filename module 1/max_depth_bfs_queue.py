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

        queue = [root]
        depth = 0

        while queue:
            depth += 1
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth
