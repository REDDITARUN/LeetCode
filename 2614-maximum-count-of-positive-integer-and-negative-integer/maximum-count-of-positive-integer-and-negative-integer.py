class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # let me assign two pointers

        def binarysearch(nums):
            left = 0
            right = len(nums)

            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < 0:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        max_neg = binarysearch(nums)
        
        max_pos = len(nums) - max_neg - nums.count(0)

        return max(max_neg, max_pos)

        