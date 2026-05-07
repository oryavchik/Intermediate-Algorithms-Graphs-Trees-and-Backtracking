"""Binary tree level order traversal"""
class TreeNode:
    """class TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        """Function init"""
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """class Solution"""
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """Function level order"""

        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
