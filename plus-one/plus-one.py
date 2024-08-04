class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Traverse the list from the end to the beginning
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, just add one and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0 and we carry over to the next digit
            digits[i] = 0
        
        # If we have traversed the whole list and all digits were 9
        return [1] + digits