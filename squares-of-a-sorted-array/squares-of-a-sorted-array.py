class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        res = [0] * n
        right = n-1
        pos = n-1
        
        while left <= right:
            lsq = nums[left] ** 2
            rsq = nums[right] ** 2
            if lsq>rsq:
                res[pos] = lsq
                left += 1
            else: 
                res[pos] = rsq
                right -= 1
            pos -=1
        
        return res
                
            
        
      
#         ne = []
#         # print(len(nums))
#         if len(nums) == 0:
#             return None
#         for i in range(len(nums)):
            
#             ne.append(nums[i] ** 2)
#         ne.sort()
#         return ne

            
        