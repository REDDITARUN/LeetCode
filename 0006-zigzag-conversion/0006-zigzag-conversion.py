class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # first we should check 
        # -- if number of rows == 1 then return 1
        # -- of if the number of rows  > num rows then return the rows
        if numRows == 1 or numRows >= len(s):
            return s         
    
    # Create a list of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Iterate through each character in the string
        for char in s:
            rows[current_row] += char
            # Change direction when you reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            current_row += 1 if going_down else -1

        # Combine rows to form the final string
        return ''.join(rows)