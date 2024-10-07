class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        lst_non = 0
        
        for  i in range( len(nums)):
            if nums[i] != 0:
                
                if i != lst_non:
                    nums[lst_non], nums[i] = nums[i],nums[lst_non]
                lst_non += 1
        
                
            
        