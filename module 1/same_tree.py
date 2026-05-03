"""Same tree"""
class TreeNode:
    """class TreeNode"""
    def __init__(self, val=0, left=None, right=None):
        """Function init"""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """class Solution"""
    def isSameTree(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode]
    ) -> bool:
        """Function is same"""

        if p is None and q is None:
            return True

        if p is None or q is None or p.val != q.val:
            return False

        left_compare = self.isSameTree(p.left, q.left)
        right_compare = self.isSameTree(p.right, q.right)

        return left_compare and right_compare
