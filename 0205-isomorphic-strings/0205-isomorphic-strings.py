class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        
        for i in range(len(s)):
                t_val = t[i]
                
                if s[i] not in dic.keys():
                    
                    if t[i] in dic.values():
                        return False
                    
                    dic[s[i]] = t_val
                elif s[i] in dic.keys() and dic[s[i]] != t[i]:
                    return False
        return True
        