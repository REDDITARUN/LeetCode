class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = - n
   
        if n == 0:
            return 1

        res = 1
        while n > 0:
            if n % 2 == 1:
                res = res * x
            x = x * x
            n = n // 2

        return res


