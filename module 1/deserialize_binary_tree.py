"""Deserialize binary tree"""
class TreeNode:
    """class TreeNode"""

    def __init__(self, x):
        """Function init"""
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """class Codec"""
    def deserialize(self, data):
        """Deserialize"""

        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1

        while queue:
            node = queue.pop(0)
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)

            i += 1

            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root
