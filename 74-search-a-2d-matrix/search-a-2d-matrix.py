class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        no_cols = len(matrix[0]) 
        no_rows = len(matrix)

        low = 0
        high = no_rows * no_cols - 1

        while low <= high:
            mid = (low + high) // 2
            mid_val = matrix[mid // no_cols][mid % no_cols]

            if mid_val == target:
                return True
            if mid_val < target:
                low = mid+1
            else:
                high = mid - 1
        return False