class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        filtered = "".join(char for char in s if char.isalnum())

        left = 0
        right = len(filtered) -1

        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        return True

        