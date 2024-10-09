class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(' ')  # Split the string into words
        
        # If the number of words doesn't match the length of the pattern, return False
        if len(pattern) != len(ss):
            return False
        
        dic = {}  # To map pattern characters to words
        reverse_map = {}  # To map words to pattern characters
        
        for i in range(len(pattern)):
            p_char = pattern[i]
            word = ss[i]
            
            # Check if pattern[i] is not mapped yet
            if p_char not in dic:
                # Check if the word is already mapped to a different pattern character
                if word in reverse_map and reverse_map[word] != p_char:
                    return False
                dic[p_char] = word
                reverse_map[word] = p_char
            # If pattern[i] is mapped, check if it's mapped to the correct word
            elif dic[p_char] != word:
                return False
        
        return True
