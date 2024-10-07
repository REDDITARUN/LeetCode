class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0
        
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k+=1
#         return k
    
    
        l = len(nums)
        k = 0
        c = 0
        for i in range(l):
            if nums[i] == val:
                nums[i] = 0
                c += 1
        nums.sort(reverse=True)
        k = l - c
        return k
        