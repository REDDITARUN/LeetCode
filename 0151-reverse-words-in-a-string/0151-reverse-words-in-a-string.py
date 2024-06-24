class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        
     
        words.reverse()
        
       
        new_string = " ".join(words)
        
        return new_string
            