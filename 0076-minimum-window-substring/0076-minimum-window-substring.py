class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        
        # Count the frequency of characters in t
        t_count = Counter(t)
        required = len(t_count)
        
        # Initialize the sliding window pointers and the necessary variables
        left, right = 0, 0
        formed = 0
        window_counts = {}
        
        # Tuple to store the result (window length, left, right)
        ans = float("inf"), None, None
        
        while right < len(s):
            # Add the current character to the window counts
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if the current character in the window matches the desired count in t
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            # Try to contract the window until it ceases to be "desirable"
            while left <= right and formed == required:
                char = s[left]
                
                # Update the result if this window is smaller than the previous best
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Remove the character from the window
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                
                # Move the left pointer ahead
                left += 1
            
            # Move the right pointer ahead
            right += 1
        
        # Return the smallest window or an empty string if no such window exists
        return "" if ans[0] == float("inf") else s[ans[1]:(ans[2] + 1)]

# Example usage:
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))  # Output: "a"
