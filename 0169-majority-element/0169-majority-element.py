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
            