class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        t_len = len(t)
        s_len = len(s)

        t_po = 0
        s_po = 0

        while  t_po < t_len and s_po < s_len:
            if s[s_po] == t[t_po]:
                s_po += 1
            
            t_po += 1
        
        return s_po == len(s)
        
        # dic = {}
        

        # for char in s:
        #     for char2 in t:
        #         if char == char2:
        #             dic[char] =  dic.get(char, t.index(char)) 

        # need to check if the dic got values in ascednng and if it's then give true or if they are not in asceding return false also we need to consifer all words in s much be present in keys of dic



        