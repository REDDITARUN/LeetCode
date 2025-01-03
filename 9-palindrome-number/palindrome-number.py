class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        if 0 <= x <= 9 :
            return True

        original = x
        reversed = 0
        
        while x > 0:
            digit = x % 10
            reversed = reversed * 10 + digit
            x = x // 10

        return original == reversed

        