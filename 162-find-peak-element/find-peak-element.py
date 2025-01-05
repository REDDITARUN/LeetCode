class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index_high = len(nums) - 1
        index_low = 0

        peak_index = 0

        while index_low < index_high:
            mid = (index_low + index_high) // 2

            if nums[mid] < nums[mid+1]:
                index_low = mid + 1
            else:
                index_high = mid 
        return index_low
        