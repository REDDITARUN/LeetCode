class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ne = []
        if len(nums) == 0:
            return None
        for i in range(len(nums)):
            ne.append(nums[i] ** 2)
        ne.sort()
        return ne
            
        