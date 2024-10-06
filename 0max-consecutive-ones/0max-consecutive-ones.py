class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        mc = 0
        if len(nums) == 0:
            return none
        for num in nums:
            if num == 1:
                count +=1
                mc = max(count, mc)
            else: count = 0


        return mc
            
        