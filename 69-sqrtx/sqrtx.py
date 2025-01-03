class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
            
        g = x // 2

        while g * g > x:
            g = (g + x // g) // 2

        return g
        