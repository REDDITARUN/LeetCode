class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # l1 = len(word1)
        # l2 = len(word2)

        # i = 0
        # res = []

        # while i < l1 and i < l2:
        #     res.append(word1[i])
        #     res.append(word2[i])
        #     i += 1
        # if l1>l2:
        #     res.extend(word1[i:])
        # elif l2>l1:
        #     res.extend(word2[i:])
        
        # return ''.join(res)
        i = 0
        j = 0
        res = []

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                res.append(word1[i])
                i += 1
            if j < len(word2):
                res.append(word2[j])
                j += 1
        return ''.join(res)

        