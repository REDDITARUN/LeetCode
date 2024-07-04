class Solution:
    def canConstruct(self, ransomNote, magazine):
        char_count = {}

        # Count the frequency of each character in magazine
        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Check if we can construct the ransomNote
        for char in ransomNote:
            if char in char_count and char_count[char] > 0:
                char_count[char] -= 1
            else:
                return False

        return True