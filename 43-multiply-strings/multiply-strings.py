class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        # Result can be at most the sum of the lengths of num1 and num2
        result = [0] * (len(num1) + len(num2))
        
        # Position in the result array
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Multiply the digits
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                # Position in the result array
                p1, p2 = i + j, i + j + 1
                # Add the multiplication result to the corresponding position
                sum_ = mul + result[p2]
                
                # Place the current digit and handle the carry
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10
        
        # Convert result to string, skip leading zeros
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0') or "0"