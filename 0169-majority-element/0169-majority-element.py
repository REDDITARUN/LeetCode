class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        store = {}
        count = len(nums)/2
        
        for ele in nums:
            if ele in store:
                store[ele] += 1
            else:
                store[ele]= 1
        
            if store[ele] > count:
                return ele
            
            
#         candidate = None
#         count = 0
        
#         for num in nums:
#             if count == 0:
#                 candidate = num
#                 count = 1
#             elif num == candidate:
#                 count += 1
#             else:
#                 count -= 1
        
#         return candidate