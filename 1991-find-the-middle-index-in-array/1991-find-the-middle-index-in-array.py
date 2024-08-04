class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        left = 0
        
        
        for i in range(n):
            right = total - left - nums[i]
            if right == left:
                return i
            left = left + nums[i]
        
        return -1
           
            
        
            
        