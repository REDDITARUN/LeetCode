class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # Step 1: Mark the presence of numbers
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        # Step 2: Collect the missing numbers
        missing_numbers = []
        for i in range(len(nums)):
            if nums[i] > 0:
                missing_numbers.append(i + 1)

        return missing_numbers

        # [-4,-2,2,-1]
        
        
#         seen = set(nums)
#         c = []
#         for i in range(1,len(nums)+1):
#             if i not in seen:
#                 c.append(i)
                
#         return c
                
                
            
            
            
        