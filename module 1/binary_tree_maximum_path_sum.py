"""Binary tree maximum path sum"""
class TreeNode:
    """class TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        """Function init"""
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """class Solution"""
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """Function max path sum"""
        max_s = float("-inf")

        def dfs(node):
            """Function dfs"""
            nonlocal max_s

            if not node:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            price = node.val + left_gain + right_gain
            max_s = max(max_s, price)

            return node.val + max(left_gain, right_gain)

        dfs(root)

        return max_s
