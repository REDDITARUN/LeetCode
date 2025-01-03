class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = min(nums)
        high = max(nums)
        while high != 0:
            low, high = high, low % high

        return low


        