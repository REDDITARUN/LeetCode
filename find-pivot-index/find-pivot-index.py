class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        left = 0
        total = sum(nums)
        
        for i in range(n):
            right = total - left - nums[i]
            if right == left:
                return i
            left = left + nums[i]
            
        return -1
        