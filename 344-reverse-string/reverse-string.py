class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s)-1
        for i in range(len(s)//2):
            s[i], s[l] = s[l], s[i]
            l-=1


        