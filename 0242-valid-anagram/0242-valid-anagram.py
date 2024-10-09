class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ss = ''.join(sorted(s))
        tt = ''.join(sorted(t))
        
        if ss == tt:
            return True
        else:
            return False
            
        