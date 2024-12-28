class Solution(object):
    def search(self, nums, target):
        index_high = len(nums) - 1
        index_low = 0

        while index_low <= index_high:
            mid_pt = int(math.floor((index_high + index_low) / 2))

            if nums[mid_pt] == target:
                return mid_pt
            if nums[mid_pt] < target:
                index_low = mid_pt + 1
            else:
                index_high = mid_pt - 1

        return -1

        