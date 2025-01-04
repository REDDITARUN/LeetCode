class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def isprime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        root = int(n ** 0.5)
        if root * root != n:
            return False
        
        return isprime(root)
        

        