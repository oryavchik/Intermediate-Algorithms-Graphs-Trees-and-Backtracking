"""Serialize binary tree"""
class TreeNode:
    """class TreeNode"""
    def __init__(self, x):
        """Function init"""
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """class Codec"""
    def serialize(self, root):
        """Serialize"""

        if not root:
            return ""

        queue = [root]
        result = []

        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")

        return ",".join(result)
