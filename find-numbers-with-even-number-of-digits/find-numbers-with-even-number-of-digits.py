class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        e = 0
        
        if len(nums) == 0:
            return None
        
        for num in nums:
            count = 0
            while num > 0:
                num //= 10
                count += 1
                
            if count%2 == 0:
                e += 1
        return e
                
        