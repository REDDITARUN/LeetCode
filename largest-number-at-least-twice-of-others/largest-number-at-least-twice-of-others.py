class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        first_largest = 0
        second_largest = 0
        n = len(nums)
        
        
        for i in range(n):
            if nums[i] > 0 and nums[i] > first_largest:
                first_largest = nums[i]
                temp = i
            for j in range(n):    
                if nums[j] > 0 and nums[j] < first_largest and nums[j] > second_largest:
                    second_largest = nums[j]
                    
        if first_largest >= 2*second_largest:
            return temp
        else:
            return -1
            

        