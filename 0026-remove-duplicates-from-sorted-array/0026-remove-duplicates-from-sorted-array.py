class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1 
        
        # chekc if there are elemments or not 
        if not nums:
            return 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
            
        return j
                
            