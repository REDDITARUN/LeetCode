class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # Special case: smallest negative number divided by -1 would cause overflow.
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values to simplify the logic
        dividend, divisor = abs(dividend), abs(divisor)

        # Perform the division using bit shifts
        quotient = 0
        # The maximum power of two we can use
        maxPower = 31
        # Compute the largest number of divisors that fits in the dividend
        while dividend >= divisor:
            # Find the maximum value of divisor * (2^power) that is <= dividend
            power = 0
            while dividend >= (divisor << (power + 1)) and (power + 1) <= maxPower:
                power += 1
            # Subtract this from the dividend
            dividend -= (divisor << power)
            # Add 2^power to the quotient
            quotient += (1 << power)
        
        # Apply the sign to the quotient
        return -quotient if negative else quotient