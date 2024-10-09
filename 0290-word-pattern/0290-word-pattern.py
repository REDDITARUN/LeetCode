class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(' ')  # Split the string into words
        
        # If the number of words doesn't match the length of the pattern, return False
        if len(pattern) != len(ss):
            return False
        
        dic = {}  # To map pattern characters to words
        mapped_words = set()  # To track already mapped words
        
        for p_char, word in zip(pattern, ss):
            if p_char not in dic:
                # Ensure no other character has already mapped to this word
                if word in mapped_words:
                    return False
                dic[p_char] = word
                mapped_words.add(word)
            elif dic[p_char] != word:
                return False
        
        return True
