class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        cur_jump = 0
        far_jump = 0
        
        for i in range (len(nums) - 1):
            far_jump = max(far_jump, i + nums[i])
            
            if i == cur_jump:
                count +=1 
                cur_jump = far_jump
                
                if cur_jump >= len(nums) - 1:
                    break
        
        return count
        
#         while cur_p < end_p:
#             val = nums[cur_p]
#             cur_p = val
#             count += 1
#             if nums[cur_p] == nums[end_p]:
#                 break
                
#         return count
            
            
            
        