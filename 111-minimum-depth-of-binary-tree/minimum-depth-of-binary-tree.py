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
        
        left_depth = float('inf')
        right_depth = float('inf')
        
        if root.left:
            left_depth = self.minDepth(root.left)

        # Calculate right depth only if right child exists
        if root.right:
            right_depth = self.minDepth(root.right)

        return min(left_depth, right_depth) + 1