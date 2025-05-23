# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def tobst(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid]) # assign the root or parent

            node.left = tobst(left, mid-1)
            node.right = tobst(mid+1,right)

            return node     
        return tobst(0, len(nums)-1)
        