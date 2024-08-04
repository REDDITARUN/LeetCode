class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num_str = ''.join(map(str, digits))
        num = int(num_str)
        
        res = num+1
        
        res_str = str(res)
        
        digits = None
        digits = [int(digit) for digit in res_str]
        
        return digits
                    
        