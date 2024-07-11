class Solution:
    def isValidSudoku(self, board):
        # Create sets to keep track of seen numbers
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                # Check the row
                if num in rows[r]:
                    return False
                rows[r].add(num)
                
                # Check the column
                if num in columns[c]:
                    return False
                columns[c].add(num)
                
                # Check the 3x3 sub-box
                box_index = (r // 3) * 3 + (c // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        return True

