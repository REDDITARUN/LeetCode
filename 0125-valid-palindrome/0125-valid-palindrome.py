class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        # Check if the filtered string is equal to its reverse
        return filtered_chars == filtered_chars[::-1]