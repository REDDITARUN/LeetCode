class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_length = 0
        left = 0
        char_index = {}
        
        for right in range(n):
            if s[right] in char_index:
                left = max(char_index[s[right]] + 1, left)
            char_index[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
