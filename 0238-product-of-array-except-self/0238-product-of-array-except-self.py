class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        # Initialize the left and right product arrays
        left_products = [1] * n
        right_products = [1] * n
        answer = [1] * n
        
        # Fill left_products array
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        
        # Fill right_products array
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
        
        # Calculate the answer array
        for i in range(n):
            answer[i] = left_products[i] * right_products[i]
        
        return answer