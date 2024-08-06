class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []

        # Dimensions of the matrix
        m, n = len(mat), len(mat[0])
        result = []
        
        # Use a dictionary to store all diagonals.
        diagonals = {}
        
        # Traverse the matrix.
        for i in range(m):
            for j in range(n):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(mat[i][j])
        
        # Collect the results, reversing the diagonals as needed.
        for k in range(m + n - 1):
            if k % 2 == 0:
                result.extend(diagonals[k][::-1])
            else:
                result.extend(diagonals[k])
        
        return result