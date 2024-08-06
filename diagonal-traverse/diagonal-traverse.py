class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
        # If the matrix is emply return the empty list
        if not mat or not mat[0]:
            return []
        
        # Check the dimensions 
        m = len(mat)            # rows
        n = len(mat[0])         # columns
        
        result = []   # empty one to store the final diag order
        diagonals = {}      # store all diagonals - key = 1 + j and value i = elements along the diagonal
        
        for i in range(m):
            for j in range(n):
                diagonal_index = i + j
                
                # If the key does not exist in the dictionary, create a new list for this diagonal.
                if diagonal_index not in diagonals:
                    diagonals[diagonal_index] = []
                
                # Append the current element mat[i][j] to the corresponding diagonal list.
                diagonals[diagonal_index].append(mat[i][j])
                
                        
                    
        # Collect the results from the diagonals dictionary.
        # There will be (m + n - 1) diagonals in total.
        
        
        for k in range(m+n-1):
            if k%2 == 0:    # If even, we need to reverse the elements in this diagonal.
                diagonal_elements = diagonals[k]
                for element in reversed(diagonal_elements):
                    result.append(element)  
            else:
                diagonal_elements = diagonals[k]
                for element in diagonal_elements:
                    result.append(element)
                    
        return result
        