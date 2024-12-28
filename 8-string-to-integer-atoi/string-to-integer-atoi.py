class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # skip the spaces
        s = s.strip()

        if not s:
            return 0

        sign = 1
        start_index = 0
        if s[0] == '-':
            sign = -1
            start_index = 1
        elif s[0] == '+':
            start_index = 1
        
        if start_index > 0 and (len(s) == start_index or not s[start_index].isdigit()):
            return 0

        res = 0
        for char in s[start_index:]:
            if not char.isdigit():
                break
            res = res * 10 + int(char)

            # Check for overflow/underflow *during* the loop
            if res > 2**31 - 1:
                return 2**31 - 1 if sign == 1 else -2**31
            if res < -2**31:
                return -2**31 if sign == -1 else 2**31-1

        return res * sign