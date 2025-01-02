# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
        

        # If one of the children is None, don't consider it (infinity ensures it won't be chosen)
        left_depth = self.minDepth(root.left) if root.left else float('inf')
        right_depth = self.minDepth(root.right) if root.right else float('inf')

        return min(left_depth, right_depth) + 1