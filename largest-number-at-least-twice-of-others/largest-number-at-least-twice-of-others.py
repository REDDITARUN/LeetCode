class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        first_largest = -1
        second_largest = -1
        largest_index = -1

        for i in range(len(nums)):
            if nums[i] > first_largest:
                second_largest = first_largest
                first_largest = nums[i]
                largest_index = i
            elif nums[i] > second_largest:
                second_largest = nums[i]

        if first_largest >= 2 * second_largest:
            return largest_index
        else:
            return -1
