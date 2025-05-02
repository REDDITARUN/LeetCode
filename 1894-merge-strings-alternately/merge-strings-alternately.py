class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)

        i = 0
        res = []

        while i < l1 and i < l2:
            res.append(word1[i])
            res.append(word2[i])
            i += 1
        if l1>l2:
            res.extend(word1[i:])
        elif l2>l1:
            res.extend(word2[i:])
        
        return ''.join(res)

        