class Solution(object):
    
    def value(self, r):
        if (r == 'I'):
            return 1
        if (r == 'V'):
            return 5
        if (r == 'X'):
            return 10
        if (r == 'L'):
            return 50
        if (r == 'C'):
            return 100
        if (r == 'D'):
            return 500
        if (r == 'M'):
            return 1000
        return -1


    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = 0 
        result = 0
        
        na = [self.value(char) for char in s]
        
        
        while i < len(na):
            if i + 1 < len(na) and na[i] < na[i+1]:
                result = result + na[i+1] - na[i]
                i+=2
            else:
                
                result = result +  na[i]
                i += 1
            

        return result