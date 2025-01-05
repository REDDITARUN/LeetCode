class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index_high = len(nums) - 1
        index_low = 0

        while index_low <= index_high:
            mid = (index_low + index_high) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                index_low = mid + 1
            else:
                index_high = mid - 1
        return index_low
        