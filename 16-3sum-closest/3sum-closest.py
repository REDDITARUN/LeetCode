class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        clos_sum = float("inf")

        for i in range(n-2):
            left = i+1
            right = n-1

            while(left < right):
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return target

                if abs(current_sum - target) < abs(clos_sum - target):
                    clos_sum = current_sum
                
                if current_sum < target:
                    left = left +1
                else:
                    right = right -1
                    
        return clos_sum