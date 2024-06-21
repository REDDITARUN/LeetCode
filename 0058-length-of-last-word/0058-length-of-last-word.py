class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.split()
        last = s[len(s)-1]
        
        return len(last)
        