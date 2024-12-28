class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
        else:
            sign = 1
        
        # Now as storing the sign completed. Next,
        x = abs(x)
        res = 0
        while x > 0:
            last_d = x % 10
            res = res * 10 + last_d
            x //= 10

        # Now as the reversing completed check the int range
        if -2**31 <= res and 2**31 - 1 >= res:
            return res*sign
        else:
            return 0