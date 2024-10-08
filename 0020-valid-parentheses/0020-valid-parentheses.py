class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2 != 0:
            return False
        
        dic={
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = []
        
        for char in s:
            if char in dic:
                stack.append(char)
            else:
                if not stack or dic[stack.pop()] != char:
                    return False
        
        if len(stack)==0:
            return True