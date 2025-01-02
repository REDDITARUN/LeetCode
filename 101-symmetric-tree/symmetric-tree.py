# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        return self.ismirr(root.left, root.right)

    def ismirr(self, left, right):
        if not left and not right:
            return True
        if not left and right:
            return False
        if not right and left:
            return False
        if right.val != left.val:
            return False
        return self.ismirr(left.left, right.right) and self.ismirr(left.right, right.left)
