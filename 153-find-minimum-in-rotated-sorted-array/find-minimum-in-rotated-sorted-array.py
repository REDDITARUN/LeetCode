class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            # Check the relationship between mid element and the high boundary
            if nums[mid] > nums[high]:
                # Minimum must be in the right part
                low = mid + 1
            else:
                # Minimum might be at mid or in the left part
                high = mid
        
        return nums[low]