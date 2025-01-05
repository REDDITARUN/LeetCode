class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findfirst(nums,target):
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = (low + high)//2
                mid_val = nums[mid]

                if mid_val < target:
                    low = mid + 1
                elif mid_val > target:
                    high = mid - 1
                else:
                    if mid == 0 or nums[mid-1] != target:
                        return mid
                    high = mid - 1
            return -1
        
        def findlast(nums,target):
            low = 0
            high = len(nums) -1

            while low <= high:
                mid = (low + high)//2
                mid_val = nums[mid]

                if mid_val < target:
                    low = mid + 1
                elif mid_val > target:
                    high = mid - 1
                else:
                    if mid == len(nums) - 1 or nums[mid+1] != target:
                        return mid
                    low = mid + 1
            return -1
        
        first = findfirst(nums, target)
        if first == -1:
            return [-1, -1]
        last = findlast(nums, target)
        return [first, last]
        
        